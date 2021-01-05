
#!/usr/bin/python3

#03/01/2021 update: for loop to trim reads + assemblies -> v4 spreadsheet (without the 'submission tool field')
#TODO: confirm that this works with output of covid-excel-utils script

import pandas as pd
import fnmatch #module for unix style pattern matching
import os #module in python provides functions for interacting with the operating system
import glob #module is used to retrieve files/pathnames matching a specified pattern
os.listdir(".") #list files and dirs in wd - make sure you are in the one where the user metadata spreadsheet will be found
files_xlsx = glob.glob("*.xlsx") #should we accept other spreadsheet extensions?

for f in files_xlsx:
    if fnmatch.fnmatch(f, '*genome*'):
        print('you are using an assembly spreadsheet')
        df = pd.read_excel(f, usecols="L:AX", header=1, sheet_name='Sheet1') #col range suits v4 
        df = df.iloc[3:,]
        df.dropna(axis=0, how='all', inplace=True)
        df.insert(7,"submission_tool",'drag and drop uploader tool',allow_duplicates=True) #study #to inject constant into trimmed df
        df.insert(24,"submission_tool",'drag and drop uploader tool',allow_duplicates=True) #sample
        print('user sample & study data below:')
        print(df)
        df.to_csv('trimmed_assembly_study_sample_metadata.csv', index=False)
    elif fnmatch.fnmatch(f, '*raw_reads*'):
        print('you are using a raw reads spreadsheet')
        df = pd.read_excel(f, usecols="B:AM", header=1, sheet_name='Sheet1') #col range suits v4
        df = df.iloc[3:,]
        df.dropna(axis=0, how='all', inplace=True)
        df.insert(7,"submission_tool",'drag and drop uploader tool',allow_duplicates=True) #study #to inject constant into trimmed df
        df.insert(24,"submission_tool",'drag and drop uploader tool',allow_duplicates=True) #sample
        print('user sample & study data below:')
        print(df)
        df.to_csv('trimmed_raw_reads_study_sample_metadata.csv', index=False)
    else:
        print('you have used an unsupported spreadsheet, please try again')
