# Xml-generator-beta
This tool creates study and sample xmls from SARS-CoV-2 metadata and submits these to the ENA. 
Validation is performed against the ERC000033 checklist: https://www.ebi.ac.uk/ena/browser/view/ERC000033

This tool is adapted from an existing tool located in this repository: https://github.com/usegalaxy-eu/ena-upload-cli . Tables and template xmls have been modified and all run and experiment data has been removed.

Please note this tool is **still in development** - although studies and samples are submittable, they are **not able to become public** at the moment.

### /example_tables 
template study and sample spreadsheets, containing corresponding metadata for upload

### /templates
required xsds and template xmls to generate study and sample xmls from

### test command to run in program directory
python3 ena_upload.py --action add --study example_tables/ENA_template_studies.tsv --sample example_tables/ENA_template_samples.tsv --center 'CENTER_NAME' --webin_id W
ebin-#### --password '#####' --dev


