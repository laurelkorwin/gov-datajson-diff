import os
import sys
from git import Repo

# Set the size limit for each Markdown file (5 MB), this is the largest github will display in its UI
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
OUTPUT_FOLDER = "readable_diffs"
SHORT_COMMIT_HASH_END = 7


def split_diff_content(diff, chunk_size):
    """Split a large diff into smaller chunks."""
    lines = diff.split("\n")
    chunks = []
    current_chunk = []
    current_size = 0

    for line in lines:
        line_size = len((line + "\n").encode("utf-8"))

        if current_size + line_size > chunk_size:
            if current_chunk:  # Only add if we have lines
                chunks.append("\n".join(current_chunk))
            current_chunk = [line]
            current_size = line_size
        else:
            current_chunk.append(line)
            current_size += line_size

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks


def generate_readme_for_json(repo_path, json_filename=None):
    """Generate README.md files showing diffs for JSON files in a Git repository."""
    repo = Repo(repo_path)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    print(f"Main output directory: {OUTPUT_FOLDER}/")

    if json_filename:
        if not os.path.isfile(json_filename):
            print(f"Error: File '{json_filename}' does not exist.")
            return
        json_files = [json_filename]
    else:
        json_files = [f for f in os.listdir(repo_path) if f.endswith(".json")]

    if not json_files:
        print("No JSON files found to process.")
        return

    for json_file in json_files:
        print(f"Processing {json_file}...")
        commits = list(repo.iter_commits(paths=json_file))
        print(f"Found {len(commits)} commits for {json_file}")

        file_dir = os.path.join(OUTPUT_FOLDER, os.path.splitext(json_file)[0])
        os.makedirs(file_dir, exist_ok=True)
        print(f"File-specific directory: {file_dir}/")

        part_number = 1
        current_filename = os.path.join(file_dir, f"changes_part{part_number}.md")

        current_content = f"# Change History for {json_file}\n\n"

        for i in range(len(commits) - 1):
            newer_commit = commits[i]
            older_commit = commits[i + 1]

            # Get diff for the JSON file, -w strips whitespace changes
            diff = repo.git.diff(
                "-w", older_commit.hexsha, newer_commit.hexsha, "--", json_file
            )

            if not diff.strip():
                continue

            # Calculate approximate chunk size (leaving room for headers)
            # Use 90% of max size to leave room for headers
            chunk_size = int(MAX_FILE_SIZE * 0.9)

            diff_chunks = split_diff_content(diff, chunk_size)

            for chunk_index, diff_chunk in enumerate(diff_chunks, 1):
                chunk_header = (
                    f"### Changes from {older_commit.hexsha[:SHORT_COMMIT_HASH_END]} to {newer_commit.hexsha[:SHORT_COMMIT_HASH_END]}"
                    f"{' (Part ' + str(chunk_index) + '/' + str(len(diff_chunks)) + ')' if len(diff_chunks) > 1 else ''}\n"
                    f"**Author:** {newer_commit.author.name}\n\n"
                    f"**Date:** {newer_commit.committed_datetime}\n\n"
                    f"**Message:** {newer_commit.message.strip()}\n\n"
                    f"```diff\n{diff_chunk}\n```\n\n"
                )

                if (
                    len((current_content + chunk_header).encode("utf-8"))
                    > MAX_FILE_SIZE
                ):
                    print(
                        f"Writing part {part_number} ({len(current_content.encode('utf-8'))} bytes)"
                    )
                    with open(current_filename, "w") as readme_file:
                        readme_file.write(current_content)

                    part_number += 1
                    current_filename = os.path.join(
                        file_dir, f"changes_part{part_number}.md"
                    )
                    current_content = (
                        f"# Change History for {json_file} (Part {part_number})\n\n"
                        + chunk_header
                    )
                else:
                    current_content += chunk_header

        if current_content.strip() != f"# Change History for {json_file}\n":
            print(
                f"Writing final part {part_number} ({len(current_content.encode('utf-8'))} bytes)"
            )
            with open(current_filename, "w") as readme_file:
                readme_file.write(current_content)

    print("\nAll JSON file histories updated!")


if __name__ == "__main__":
    """
    Run with a specific file:
        python generate_diff_readmes.py ed.json
    Run with all files:
        python generate_diff_readmes.py
    """
    if len(sys.argv) > 1:
        generate_readme_for_json(os.getcwd(), sys.argv[1])
    else:
        generate_readme_for_json(os.getcwd())
