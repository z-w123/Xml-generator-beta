
#!/usr/bin/python3

#24/02/2021 update: v4 spreadsheet (without the 'submission tool field') units row formatting
#TODO: confirm that this works with output of covid-excel-utils script

import pandas as pd
import fnmatch #module for unix style pattern matching
import os #module in python provides functions for interacting with the operating system
import glob #module is used to retrieve files/pathnames matching a specified pattern
os.listdir(".") #list files and dirs in wd - make sure you are in the one where the user metadata spreadsheet will be found
files_xlsx = glob.glob("*.xlsx") #should we accept other spreadsheet extensions? #will remove this for now to accept only specific spreadsheet name

for f in files_xlsx:
    if fnmatch.fnmatch(f, '*genome*'):
        print('you are using an assembly spreadsheet')
        df = pd.read_excel(f, usecols="L:AV", header=1, sheet_name='Sheet1') #col range suits v4 
        df = df.iloc[2:,]
        df.dropna(axis=0, how='all', inplace=True)
        df.insert(7,"submission_tool",'drag and drop uploader tool',allow_duplicates=True) #study #to inject constant into trimmed df
        df.insert(24,"submission_tool",'drag and drop uploader tool',allow_duplicates=True) #sample
        df.insert(26,"sample capture status",'active surveillance in response to outbreak',allow_duplicates=False)
        df.iloc[0, df.columns.get_loc('submission_tool')] = 'NaN' #effectively removes the 'drag and drop uploader tool' value from units row, by replacing with NaN
        df.iloc[0, df.columns.get_loc('sample capture status')] = 'NaN' #see above
        df.rename(columns = {'collecting institute':'collecting institution'}, inplace = True)
        print('user sample & study data below:')
        print(df)
        df.to_csv('trimmed_assembly_study_sample_metadata_21_feb.csv', index=False)
    elif fnmatch.fnmatch(f, '*raw_reads*'):
        print('you are using a raw reads spreadsheet')
        df = pd.read_excel(f, usecols="B:AL", header=1, sheet_name='Sheet1') #col range suits v4
        df = df.iloc[2:,]
        df.dropna(axis=0, how='all', inplace=True)
        df.insert(7,"submission_tool",'drag and drop uploader tool',allow_duplicates=True) #study #to inject constant into trimmed df
        df.insert(24,"submission_tool",'drag and drop uploader tool',allow_duplicates=True) #sample
        df.insert(26,"sample capture status",'active surveillance in response to outbreak',allow_duplicates=False)
        df.iloc[0, df.columns.get_loc('submission_tool')] = '' #effectively removes the 'drag and drop uploader tool' value from units row, by replacing with NaN
        df.iloc[0, df.columns.get_loc('sample capture status')] = '' #see above
        df.rename(columns = {'collecting institute':'collecting institution'}, inplace = True)
        print('user sample & study data below:')
        print(df)
        df.to_csv('trimmed_raw_reads_study_sample_metadata_21_feb_test.csv', index=False)
    else:
        print('you have used an unsupported spreadsheet, please try again')
