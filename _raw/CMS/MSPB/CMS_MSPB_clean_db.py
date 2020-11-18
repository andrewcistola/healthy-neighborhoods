# allocativ
# Healthy Neighborhoods
# CMS Hospital Compare 2018 and 2019

## Import Libraries and Data

### Import Python libraries
import os # Operating system navigation
import sqlite3 # SQLite database manager

### Import data science libraries
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'

### Set working directory
os.chdir("C:/Users/drewc/GitHub/allocativ") # Set wd to project repository

## Clean raw data

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/MSPB_2018/Medicare_Spending_Per_Beneficiary___Hospital.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository

### Clean outcome data
df_clean = df_raw.filter(["Score", "Facility ID", "ZIP Code"]) # Keep only selected columns
df_clean = df_clean.rename(columns = {"Score": "MSPB", "Facility ID": "Facility_ID", "ZIP Code": "ZIP"}) # Rename multiple columns in place
df_clean["MSPB"] = df_clean["MSPB"].apply(pd.to_numeric, errors = "coerce") # Change data type of column in data frame
df_clean = df_clean.dropna() # Drop all rows with NA values

### Veirfy
df_clean.info() # Get class, memory, and column info: names, data types, obs.
df_clean.head() # Print first 5 observations

## Step 2: Prepare clean data for HNB database

### Import HNB key dataset
df_key = pd.read_csv("hnb/FIPS/FIPS_ZCTA_key.csv") # Import dataset saved as csv in _data folder

### Create HNB ZCTA key
df_ZCTA = df_clean
df_ZCTA['ZCTA'] = df_ZCTA['ZIP'].astype("str") # Change data type of column in data frame
df_ZCTA['ZCTA'] = df_ZCTA['ZCTA'].str.rjust(5, "0") # add leading zeros of character column using rjust() function
df_ZCTA['ZCTA'] = "ZCTA"+ df_ZCTA['ZCTA'] # Combine string with column
df_ZCTA = df_ZCTA.drop(columns = ["ZIP"]) # Drop Unwanted Columns

### Join with FIPS and ST
df_key = df_key.filter(["ZCTA", "FIPS", "ST"]) # Keep only selected columns
df_ZCTA = pd.merge(df_key, df_ZCTA, on = "ZCTA", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Reorder HNB keys
first = df_ZCTA.pop("ZCTA") # 'pop' column from df
df_ZCTA.insert(0, "ZCTA", first) # reinsert in index

### Veirfy
df_ZCTA.info() # Get class, memory, and column info: names, data types, obs.
df_ZCTA.head() # Print first 5 observations

## Step 3: Export to csv and SQLite database

### Export full, percent estimate, and label tables
df_ZCTA.to_csv(r"hnb/CMS/MSPB_2018/CMS_2018_MSPB_ZCTA.csv") # Export df as csv

### Conenct to database
con = sqlite3.connect('hnb/_database/HNB.db')
df_ZCTA.to_sql('CMS_2018_MSPB', con, if_exists = 'replace', index = False)