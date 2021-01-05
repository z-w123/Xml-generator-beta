# Xml-generator-version 2

### Part 1: Trimming_metadata_spreadsheet .py
This script has two functions:
1. trims the user metadata spreadsheet to exclude everything other than study and sample metadata
2. injects the 'submission_tool' field (With value: 'drag and drop uploader tool') into study and sample sections of the trimmed spreadsheet

The trimmed spreadsheet then feeds into part 2 of the script which generates the xml (to be added to repo)
