# Xml-generator-version 2
The Xml-generator tool creates study and sample (and submission) xmls for programmatic submission of SARS-CoV-2 data to the ENA, validating against the ERC000033 checklist.

### Part 1: Trimming_metadata_spreadsheet .py
This script has three functions:
1. trims the user metadata spreadsheet to exclude everything other than study and sample metadata
2. injects the 'submission_tool' field (With value: 'drag and drop uploader tool') into study and sample sections of the trimmed spreadsheet
3. injects the 'sample capture status' field (with value: 'active surveillance in response to outbreak') into the sample section

The trimmed spreadsheet then feeds into part 2 of the script which generates the study and sample xmls

### Part 2: ena-metadata-xml-generator_v4.py
This script has the following functions:
1. Creates study, sample and submission xmls using the output of Part 1
2. Validates and submits the xmls using curl
