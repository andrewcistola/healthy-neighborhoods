#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Neville Subproject: Using Random Forestes, Factor Analysis, and Logistic regression to Screen Variables for Imapcts on Public Health
## NHANES 2005-2006: Connecting Diabetes and Colorectal Cancer
# The Python Programming Langauge Script by DrewC!

#### Section A: Import Libraries, Import Dataset, Prepare for Classification

### Step 1: Import Libraries and Import Dataset

## Import Standard Libraries
import os # Inlcuded in every script DC!
import numpy as np # Inclduded in every code script DC!
import pandas as pd # Incldued in every code script for DC!
import scipy as sp # Incldued in every code script for DC!

## Import Dataset
os.chdir("C:/Users/drewc/Dropbox (UFL)/Public Data Sources/NHANES/2005-2006") # Set wd to project repository
df_names = pd.read_csv("CMD/raw_filename.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository

## Tidy Data

## Verify
df_names.head() # Get class, memory, and column info: names, data types, obs.
df_names.head() # Print first 5 observations
df_names.shape # Print dimensions of data frame

### Step 2: Automate File Creation Process

## Create SAS Code Text File
text_file = open("CODE/NHANES_DOWNLOAD_2005-2006.txt", "w") # Open text file and name with subproject, content, and result suffix
text_file.write("*** NHANES 2015-2016\n")
text_file.write("** Full Cohort download, export, and join code script\n")
text_file.write("* The following code uses directions on NHANES Data tutorial\n")
text_file.write("* https://www.cdc.gov/nchs/tutorials/NHANES/preparing/download/intro.htm;\n\n")
text_file.write('libname DT "C:\\Users\\drewc\\Dropbox (UFL)\\Public Data Sources\\NHANES\\2005-2006\\DATA";\n')
text_file.write('libname XP "C:\\Users\\drewc\\Dropbox (UFL)\\Public Data Sources\\NHANES\\2005-2006\\XP";\n')
text_file.write('libname EX "C:\\Users\\drewc\\Dropbox (UFL)\\Public Data Sources\\NHANES\\2005-2006\\EXPORT";\n')
text_file.write("run;\n\n")
text_file.close() # Close file

## Convert XP files to SAS data files 
l_xpt = df_names["XPT"] # Save as list

## Write SAS Code for XP transfer
for Q in l_xpt:
    text_file = open("CODE/NHANES_DOWNLOAD_2005-2006.txt", "a")
    text_file.write('libname XP xport "C:\\Users\\drewc\\Dropbox (UFL)\\Public Data Sources\\NHANES\\2005-2006\\XP\\') 
    text_file.write(Q)
    text_file.write('";\n')
    text_file.write("proc copy in = XP out = DT;\n")
    text_file.write("run;\n\n")
    text_file.close()

## Run Text Code in SAS

## Import names of Data files
df_SAS = pd.read_csv("CMD/SAS_filename.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_SAS["DT"] = df_SAS["SAS"].str.replace(r".sas7bdat$", "")
df_SAS["DT"] = "DT." + df_SAS["DT"]
l_DT = df_SAS["DT"]
str_DT = " ".join(l_DT)

## Sort by SEQN Variable
for Q in l_DT:
    text_file = open("CODE/NHANES_DOWNLOAD_2005-2006.txt", "a")
    text_file.write('proc sort data = ') 
    text_file.write(Q)
    text_file.write(";\n")
    text_file.write("by SEQN;\n")
    text_file.write("run;\n\n")
    text_file.close()

## Sort by SEQN Variable
text_file = open("CODE/NHANES_DOWNLOAD_2005-2006.txt", "a")
text_file.write("data EX.full;\n")
text_file.write("merge\n")
text_file.write(str_DT)
text_file.write(";\n")
text_file.write("by SEQN;\n")
text_file.write("run;\n\n")
text_file.close()

## Export SAS Dataset to CSV;
text_file = open("CODE/NHANES_DOWNLOAD_2005-2006.txt", "a")
text_file.write("proc export data = EX.full dbms = csv\n")
text_file.write('outfile = "C:\\Users\\drewc\\Dropbox (UFL)\\Public Data Sources\\NHANES\\2005-2006\\EXPORT\\nhanes_1516_exam_raw.csv"\n')
text_file.write("replace;\n")
text_file.write("run;\n\n")
text_file.close()


## Run Text Code in SAS

