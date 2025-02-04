import os
import time
import tiktoken
import argparse
from anthropic import Anthropic, APIError, RateLimitError
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

MAX_TOKENS = 35000  # Need to stay under Claude API rate limit (40k/minute)
OUTPUT_FOLDER = "readable_diffs"
MODEL = "claude-3-5-sonnet-20241022"
RATE_LIMIT_WAIT = (
    62  # 1 minute and 2 seconds in seconds, since rate limit is per minute
)
MAX_RETRIES = 3


def retry_on_rate_limit(func):
    """Decorator to handle rate limit errors with retry logic."""

    def wrapper(*args, **kwargs):
        retries = 0
        while retries < MAX_RETRIES:
            try:
                return func(*args, **kwargs)
            except RateLimitError as e:
                retries += 1
                print(
                    f"\nRate limit hit. Waiting {RATE_LIMIT_WAIT} seconds before retry {retries}/{MAX_RETRIES}..."
                )
                time.sleep(RATE_LIMIT_WAIT)
                print("Retrying...")
                continue
            except APIError as e:
                if "rate_limit" in str(e).lower():
                    retries += 1
                    print(
                        f"\nRate limit hit. Waiting {RATE_LIMIT_WAIT} seconds before retry {retries}/{MAX_RETRIES}..."
                    )
                    time.sleep(RATE_LIMIT_WAIT)
                    print("Retrying...")
                    continue
                raise e
            except Exception as e:
                print(f"Unexpected error: {str(e)}")
                raise e

        print(f"Failed after {MAX_RETRIES} retries")
        return None

    return wrapper


def count_tokens(text):
    """Estimate token count using tiktoken."""
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


def load_and_batch_files(folder_path):
    """Load markdown files and batch them by token count."""
    files_content = []
    current_batch = []
    current_batch_tokens = 0
    prompt_overhead = count_tokens("File analysis prompt and formatting overhead")

    files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])

    for filename in files:
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                content_tokens = count_tokens(content)

                # If this single file is too large, we need to split it
                if content_tokens > MAX_TOKENS:
                    lines = content.split("\n")
                    chunk_content = []
                    chunk_tokens = 0
                    for line in lines:
                        line_tokens = count_tokens(line + "\n")
                        if chunk_tokens + line_tokens > MAX_TOKENS - prompt_overhead:
                            if chunk_content:
                                files_content.append(
                                    [
                                        {
                                            "filename": f"{filename}_part{len(files_content)}",
                                            "content": "\n".join(chunk_content),
                                            "tokens": chunk_tokens,
                                        }
                                    ]
                                )
                            chunk_content = [line]
                            chunk_tokens = line_tokens
                        else:
                            chunk_content.append(line)
                            chunk_tokens += line_tokens

                    if chunk_content:
                        files_content.append(
                            [
                                {
                                    "filename": f"{filename}_part{len(files_content)}",
                                    "content": "\n".join(chunk_content),
                                    "tokens": chunk_tokens,
                                }
                            ]
                        )
                    continue

                # For normal-sized files, batch them together
                if (
                    current_batch_tokens + content_tokens > MAX_TOKENS - prompt_overhead
                    and current_batch
                ):
                    files_content.append(current_batch)
                    current_batch = []
                    current_batch_tokens = 0

                current_batch.append(
                    {"filename": filename, "content": content, "tokens": content_tokens}
                )
                current_batch_tokens += content_tokens
        except Exception as e:
            print(f"Error reading file {filename}: {str(e)}")
            continue

    if current_batch:
        files_content.append(current_batch)

    return files_content


@retry_on_rate_limit
def analyze_batch_with_claude(client, batch, folder_name):
    """Analyze a batch of files using Claude API."""
    content = "\n\n---\n\n".join(
        f"File: {file['filename']}\n\n{file['content']}" for file in batch
    )

    prompt = f"""Analyze these git diff changes from {folder_name} and provide:
    1. A summary of the key changes
    2. Note any consistent patterns in terminology modifications, including:
       - Words or phrases that are consistently replaced with alternatives
       - Terms that are added or removed systematically
       - Changes in how concepts are described or referenced
    3. Notable structural or organizational changes in the content

    Changes to analyze:

    {content}"""

    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        temperature=0,
        messages=[{"role": "user", "content": prompt}],
    )

    return (
        response.content[0].text
        if isinstance(response.content, list)
        else response.content
    )


@retry_on_rate_limit
def aggregate_folder_summary(client, batch_summaries, folder_name):
    """Create an aggregated summary from all batch summaries."""
    prompt = f"""Create a comprehensive summary of git diff changes in the {folder_name} folder that:
    1. Identifies the major themes and patterns in the changes
    2. Documents any systematic changes in terminology or language choices
    3. Provides a high-level overview of both content and structural modifications

    Batch summaries:

    {batch_summaries}"""

    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        temperature=0,
        messages=[{"role": "user", "content": prompt}],
    )

    return (
        response.content[0].text
        if isinstance(response.content, list)
        else response.content
    )


def analyze_folder(folder_name):
    """Analyze a single folder's changes."""
    try:
        client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    except Exception as e:
        print(f"Error initializing Anthropic client: {str(e)}")
        return

    folder_path = os.path.join(OUTPUT_FOLDER, folder_name)
    if not os.path.exists(folder_path):
        print(f"Error: Folder {folder_path} not found")
        return
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a directory")
        return

    print(f"\nProcessing {folder_name} folder...")

    summary_dir = os.path.join(folder_path, "summaries")
    os.makedirs(summary_dir, exist_ok=True)

    batches = load_and_batch_files(folder_path)
    batch_summaries = []

    for i, batch in enumerate(batches, 1):
        print(f"Analyzing batch {i}/{len(batches)} for {folder_name}...")
        total_tokens = sum(file["tokens"] for file in batch)
        print(f"Batch {i} token count: {total_tokens}")

        if total_tokens >= MAX_TOKENS:
            print(f"Warning: Batch {i} is too large ({total_tokens} tokens)")
            continue

        summary = analyze_batch_with_claude(client, batch, folder_name)

        # Only process and save if we got a successful response
        if summary is not None:
            batch_summaries.append(summary)

            batch_summary_file = os.path.join(summary_dir, f"batch_{i}_summary.md")
            with open(batch_summary_file, "w", encoding="utf-8") as f:
                f.write(f"# Batch {i} Summary\n\n")
                f.write(
                    f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                )
                f.write(f"Total tokens in batch: {total_tokens}\n\n")
                f.write(summary)
        else:
            print(f"Failed to analyze batch {i} after retries")

    if batch_summaries:
        print(f"Creating folder-level summary for {folder_name}...")
        folder_summary = aggregate_folder_summary(
            client, "\n\n".join(batch_summaries), folder_name
        )

        # Only save if we got a successful response
        if folder_summary is not None:
            folder_summary_file = os.path.join(summary_dir, "folder_summary.md")
            with open(folder_summary_file, "w", encoding="utf-8") as f:
                f.write(f"# {folder_name} Folder Summary\n\n")
                f.write(
                    f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                )
                f.write(folder_summary)
        else:
            print("Failed to create folder summary after retries")

    print(f"Completed analysis for {folder_name}")


def main():
    """
    Analyze changes in readable_diffs folder using Claude API.

    Usage:
        python claude_analyzer.py [folder_name]

    Example:
        python claude_analyzer.py usaid
        python claude_analyzer.py ed

    The script will process all markdown files in readable_diffs/[folder_name]/
    and generate summaries in readable_diffs/[folder_name]/summaries/
    """
    parser = argparse.ArgumentParser(
        description="Analyze changes in a specific folder using Claude API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=main.__doc__,
    )
    parser.add_argument(
        "folder_name", help="Name of the folder under readable_diffs to analyze"
    )
    args = parser.parse_args()

    if not os.path.exists(OUTPUT_FOLDER):
        print(f"Error: {OUTPUT_FOLDER} directory not found")
        return

    analyze_folder(args.folder_name)


if __name__ == "__main__":
    main()
