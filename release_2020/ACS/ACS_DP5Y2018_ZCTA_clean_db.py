# allocativ
# Healthy Neighborhoods
# ACS DP5Y2018 join Code
# Fl ZCTA subset code

## Import Libraries and Data

### Import Python libraries
import os # Operating system navigation
import sqlite3 # SQLite database manager

### Import data science libraries
import numpy as np # Widely used matrix library for numerical processes
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'

### Set working directory
os.chdir("C:/Users/drewc/GitHub/allocativ") # Set wd to project repository

## DP02
df_DP = pd.read_csv("hnb/ACS/DP5Y2018/DP02/ACSDP5Y2018.DP02_data_with_overlays_2020-06-30T110936.csv", low_memory = 'false') # Import dataset saved as csv in _data folder

### Standardize geo keys
df_DP['ZCTA'] = df_DP['NAME'].str.replace("5 ","") # Strip all spaces from column in data frame
df_DP = df_DP.drop(columns = ["NAME", "GEO_ID"]) # Drop Unwanted Columns
df_DP.loc[0, 'ZCTA'] = 'Five digit zip code' # Change value in dataframe by index and column

### Separate labels
df_DP02_l = df_DP.loc[0, :] # Save selection of rows with all columns as df
df_DP02_l = pd.DataFrame(df_DP02_l) # Save as Pandas dataframe

### Create percent estimate table
df_DP = df_DP.drop(0) # Drop row in data frame by index
df_DP = df_DP.set_index("ZCTA") # Set column as index
df_DP = df_DP.loc[:, df_DP.columns.str.contains('PE')] # Select columns by string value
df_DP = df_DP.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric

### Join with key
df_key = pd.read_csv("hnb/FIPS/FIPS_ZCTA_key.csv") # Import dataset saved as csv in _data folder
df_key = df_key.filter(["FIPS", "ZCTA", "ST"]) # Keep only selected columns
df_DP = pd.merge(df_key, df_DP, on = "ZCTA", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Verify
df_DP02 = df_DP 
df_DP02.info() # Get class, memory, and column info: names, data types, obs.
df_DP02.head() # Print first 5 observations

## DP03
df_DP = pd.read_csv("hnb/ACS/DP5Y2018/DP03/ACSDP5Y2018.DP03_data_with_overlays_2020-06-30T103908.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Standardize geo keys
df_DP['ZCTA'] = df_DP['NAME'].str.replace("5 ","") # Strip all spaces from column in data frame
df_DP = df_DP.drop(columns = ["NAME", "GEO_ID"]) # Drop Unwanted Columns
df_DP.loc[0, 'ZCTA'] = 'Five digit zip code' # Change value in dataframe by index and column

### Separate labels
df_DP03_l = df_DP.loc[0, :] # Save selection of rows with all columns as df
df_DP03_l = pd.DataFrame(df_DP03_l) # Save as Pandas dataframe

### Create percent estimate table
df_DP = df_DP.drop(0) # Drop row in data frame by index
df_DP = df_DP.set_index("ZCTA") # Set column as index
df_DP = df_DP.loc[:, df_DP.columns.str.contains('PE')] # Select columns by string value
df_DP = df_DP.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric

### Join with key
df_key = pd.read_csv("hnb/FIPS/FIPS_ZCTA_key.csv") # Import dataset saved as csv in _data folder
df_key = df_key.filter(["FIPS", "ZCTA", "ST"]) # Keep only selected columns
df_DP = pd.merge(df_DP, df_key, on = "ZCTA", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Verify
df_DP03 = df_DP 
df_DP03.info() # Get class, memory, and column info: names, data types, obs.
df_DP03.head() # Print first 5 observations

## DP04
df_DP = pd.read_csv("hnb/ACS/DP5Y2018/DP04/ACSDP5Y2018.DP04_data_with_overlays_2020-07-01T093051.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Standardize geo keys
df_DP['ZCTA'] = df_DP['NAME'].str.replace("5 ","") # Strip all spaces from column in data frame
df_DP = df_DP.drop(columns = ["NAME", "GEO_ID"]) # Drop Unwanted Columns
df_DP.loc[0, 'ZCTA'] = 'Five digit zip code' # Change value in dataframe by index and column

### Separate labels
df_DP04_l = df_DP.loc[0, :] # Save selection of rows with all columns as df
df_DP04_l = pd.DataFrame(df_DP04_l) # Save as Pandas dataframe

### Create percent estimate table
df_DP = df_DP.drop(0) # Drop row in data frame by index
df_DP = df_DP.set_index("ZCTA") # Set column as index
df_DP = df_DP.loc[:, df_DP.columns.str.contains('PE')] # Select columns by string value
df_DP = df_DP.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric

### Join with key
df_key = pd.read_csv("hnb/FIPS/FIPS_ZCTA_key.csv") # Import dataset saved as csv in _data folder
df_key = df_key.filter(["FIPS", "ZCTA", "ST"]) # Keep only selected columns
df_DP = pd.merge(df_DP, df_key, on = "ZCTA", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Verify
df_DP04 = df_DP 
df_DP04.info() # Get class, memory, and column info: names, data types, obs.
df_DP04.head() # Print first 5 observations

## DP05
df_DP = pd.read_csv("hnb/ACS/DP5Y2018/DP05/ACSDP5Y2018.DP05_data_with_overlays_2020-06-30T101728.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Standardize geo keys
df_DP['ZCTA'] = df_DP['NAME'].str.replace("5 ","") # Strip all spaces from column in data frame
df_DP = df_DP.drop(columns = ["NAME", "GEO_ID"]) # Drop Unwanted Columns
df_DP.loc[0, 'ZCTA'] = 'Five digit zip code' # Change value in dataframe by index and column

### Separate labels
df_DP05_l = df_DP.loc[0, :] # Save selection of rows with all columns as df
df_DP05_l = pd.DataFrame(df_DP05_l) # Save as Pandas dataframe

### Create percent estimate table
df_DP = df_DP.drop(0) # Drop row in data frame by index
df_DP = df_DP.set_index("ZCTA") # Set column as index
df_DP = df_DP.loc[:, df_DP.columns.str.contains('PE')] # Select columns by string value
df_DP = df_DP.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric

### Join with key
df_key = pd.read_csv("hnb/FIPS/FIPS_ZCTA_key.csv") # Import dataset saved as csv in _data folder
df_key = df_key.filter(["FIPS", "ZCTA", "ST"]) # Keep only selected columns
df_DP = pd.merge(df_DP, df_key, on = "ZCTA", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Verify
df_DP05 = df_DP 
df_DP05.info() # Get class, memory, and column info: names, data types, obs.
df_DP05.head() # Print first 5 observations

## Create Tables for SQLlite Database

### Merge Join Group in data frame
df_DP03 = df_DP03.drop(columns = ["FIPS", "ST"]) # Drop Unwanted Columns
df_DP = pd.merge(df_DP02, df_DP03, on = "ZCTA", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options
df_DP04 = df_DP04.drop(columns = ["FIPS", "ST"]) # Drop Unwanted Columns
df_DP = pd.merge(df_DP, df_DP04, on = "ZCTA", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options
df_DP05 = df_DP05.drop(columns = ["FIPS", "ST"]) # Drop Unwanted Columns
df_DP = pd.merge(df_DP, df_DP05, on = "ZCTA", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Drop features with less than 75% data
df_DP = df_DP.dropna(axis = 1, thresh = 0.75*len(df_DP)) # Drop features less than 75% non-NA count for all columns

### Export to csv
df_DP.to_csv(r"hnb/ACS/DP5Y2018/ACS_DP5Y2018_ZCTA_full.csv") # Export df as csv

### Conenct to database
con = sqlite3.connect('hnb/_database/HNB.db')
df_DP.to_sql('ACS_DP5Y2018_ZCTA', con, if_exists='replace', index = False)

### Stack dataframes
df_DP_l = pd.concat([df_DP02_l, df_DP03_l]) # Combine rows with same columns
df_DP_l = pd.concat([df_DP_l, df_DP04_l]) # Combine rows with same columns
df_DP_l = pd.concat([df_DP_l, df_DP05_l]) # Combine rows with same columns

### Label tables
df_DP_l.to_csv(r"hnb/ACS/DP5Y2018/ACS_DP5Y2018_ZCTA_labels.csv") # Export df as csv


### Debug Fix: Add Labels after gini and avg calcs
df_labels = pd.read_csv("hnb/ACS/DP5Y2018/ACS_DP5Y2018_ZCTA_labels.csv", low_memory = 'false') # Import dataset saved as csv in _data folder
df_labels =  df_labels.rename(columns = {"Unnamed: 0": "Code", "0": "Label"}) # Rename multiple columns in place
df_labels = df_labels[df_labels["Code"].str.contains("PE")] # Subset character column by string
df_labels['Label'] = df_labels['Label'].str.replace(" ","") # Strip all spaces from column in data frame
df_labels['Label'] = df_labels['Label'].str.replace("!!","") # Strip all spaces from column in data frame
df_labels['Label'] = df_labels['Label'].str.replace("PercentEstimate","") # Strip all spaces from column in data frame

df_gini = df_labels
df_gini["Code"] = df_gini["Code"] + "_gini" # Subset character column by string
df_gini["Label"] = df_gini["Label"] + "Gini" # Subset character column by string

df_avg = df_labels
df_avg["Code"] = df_avg["Code"] + "_avg" # Subset character column by string
df_avg["Label"] = df_avg["Label"] + "AVG" # Subset character column by string

df_lab = pd.concat([df_avg, df_gini]) # Combine rows with same columns
new_row = {'Code':'FIPS', 'Label':'FIPS'}
df_lab = df_lab.append(new_row, ignore_index = True)

df_lab.to_csv(r"hnb/ACS/DP5Y2018/ACS_DP5Y2018_FIPS_labels.csv") # Export df as csv

df_acs = pd.read_csv("hnb/ACS/DP5Y2018/ACS_DP5Y2018_FIPS_gini.csv", low_memory = 'false') # Import dataset saved as csv in _data folder
df_acs = df_acs.transpose() # Transpose Rows and Columns
df_acs = df_acs.reset_index() # Reset Index
df_acs =  df_acs.rename(columns = {"index": "Label"}) # Rename multiple columns in place

df_join = pd.merge(df_acs, df_lab, on = "Label", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = df_join.drop(columns = ["Code"]) # Drop Unwanted Columns
df_join = df_join.transpose() # Transpose Rows and Columns
df_join.columns = df_join.iloc[3137]
df_join = df_join.drop(index = "Code")
df_join = df_join.drop(index = "Label")
df_join = df_join.sort_values(by = ["FIPS"], ascending = True) # Sort Columns by Value

df_join.to_csv(r"hnb/ACS/DP5Y2018/ACS_DP5Y2018_FIPS_gini.csv") # Export df as csv


df_join = pd.merge(df_acs, df_lab, on = "Code", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

#### Keep only precent estimate labels - 16 Oct 2020 Linux

df_label = pd.read_csv("/home/drewc/GitHub/covid-florida/_geo/_raw/ACS_DP5Y2018/ACS_DP5Y2018_ZCTA_labels.csv") # Import dataset saved as csv in _data folder
df_label =  df_label.rename(columns = {"Unnamed: 0": "Code", "0": "Label"}) # Rename multiple columns in place
df_label = df_label.astype("string") # Change data type of column in data frame
df_label = df_label[df_label["Code"].str.contains("PE")] # Subset character column by string
df_label['Full'] = df_label['Label']
df_label['Label'] = df_label['Label'].str.replace('Percent Estimate!!','') # Strip all spaces from column in data frame
df_label['Label'] = df_label['Label'].str.replace('!!',' ') # Strip all spaces from column in data frame

df_label.head() # Print first 5 observations
df_label.info() # Get class, memory, and column info: names, data types, obs.

df_label.to_csv(r"/home/drewc/GitHub/covid-florida/_geo/_raw/ACS_DP5Y2018/ACS_DP5Y2018_ZCTA__PE_labels.csv") # Export df as csv




