# gov-datajson-diff

This fork adds functionality to the gov-datajson-diff repo to:
- make the JSON file data diffs human readable in a browser
- enable querying Claude for summarizing of the data diffs

<h2>Making diffs readable in browser</h2>
Github limits viewing of files in browser to those < 1mb.

To adhere to this limit, `generate_diff_readmes.py` 
loads the diffs, by commit, with GitPython and chunks them into
subfiles to remain under the file size limit. 

The chunked files are viewable 
under `readable_diffs`, segmented by folders that correspond to the JSON file names.

<h2>Claude summaries of changes</h2>
The script, `claude_analyzer.py`, enables querying the Claude API with the diffs, by folder,
to analyze overall changes. 

It first chunks the diffs into segments that fit below the API rate limit (40k tokens / minute).

Next, it generates a summary for each segment "batch", and finally combines the batch summaries to generate
a summary for the entire folder.

The summaries (batch level and folder level) for each json data file are viewable under `readable_diffs/[folder_name]/summaries`.

<h2>Running locally</h2>
To run locally, you can use [poetry](https://python-poetry.org/docs/basic-usage/) for dependency management.
You'll need to have a Claude API key, and expose it in your own `.env` file at the top package level (do not commit it please! 😅)