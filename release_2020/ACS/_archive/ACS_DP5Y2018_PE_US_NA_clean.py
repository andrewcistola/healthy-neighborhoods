# allocativ
# Healthy Neighborhoods
# ACS DP5Y2018 Join Code
# ACS DP5Y2018 PE US NA Clean Code

## Import Libraries and Data

### Import Python libraries
import os # Operating system navigation

### Import data science libraries
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'

### Set working directory
os.chdir("C:/Users/drewc/GitHub/allocativ/hnb/ACS/DP5Y2018") # Set wd to project repository

### Import ACS datasets from csv files
df_key = pd.read_csv("C:/Users/drewc/GitHub/allocativ/hnb/FIPS/FIPS_ZCTA_key.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Import ACS datasets from csv files
df_DP02 = pd.read_csv("DP02/ACSDP5Y2018.DP02_data_with_overlays_2020-06-30T110936.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_DP03 = pd.read_csv("DP03/ACSDP5Y2018.DP03_data_with_overlays_2020-06-30T103908.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_DP04 = pd.read_csv("DP04/ACSDP5Y2018.DP04_data_with_overlays_2020-07-01T093051.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_DP05 = pd.read_csv("DP05/ACSDP5Y2018.DP05_data_with_overlays_2020-06-30T101728.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

## Create Full ACS table and variable key

### Remove duplicate NAME columns
df_DP02["GEO_NAME"] = df_DP02["NAME"] # Rename column in data frame
df_DP02 = df_DP02.drop(columns = ["NAME"]) # Drop Unwanted Columns
df_DP03 = df_DP03.drop(columns = ["NAME"]) # Drop Unwanted Columns
df_DP04 = df_DP04.drop(columns = ["NAME"]) # Drop Unwanted Columns
df_DP05 = df_DP05.drop(columns = ["NAME"]) # Drop Unwanted Columns

### Merge Join Group in data frame
df_join = pd.merge(df_DP02, df_DP03, on = "GEO_ID", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join2 = pd.merge(df_DP04, df_join, on = "GEO_ID", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options
df_full = pd.merge(df_DP05, df_join2, on = "GEO_ID", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Add standardized keys
df_full['ZCTA'] = df_full['GEO_NAME'].str.replace("5 ","") # Strip all spaces from column in data frame
df_full['FIPS'] = df_full['GEO_ID'] # Add new column as duplicate of other column
df_full.loc[0, 'FIPS'] = 'FIPS Code' # Change value in dataframe by index and column
df_full.loc[0, 'ZCTA'] = 'Five digit zip code' # Change value in dataframe by index and column

### Create feature label table
df_label = df_full.loc[0, :] # Save selection of rows with all columns as df
df_full = df_full.drop(0) # Drop row in data frame by index

### Create population crosswalk file
df_pop = df_full.filter(["DP05_0001E", "ZCTA"]) # Keep only selected columns

### Verify 
df_full.info() # Get class, memory, and column info: names, data types, obs.
df_full.head() # Print first 5 observations

### Export full, percent estimate, and label tables
df_label.to_csv(r"ACS_DP5Y2018_label.csv") # Export df as csv
df_full.to_csv(r"ACS_DP5Y2018_full.csv") # Export df as csv
df_pop.to_csv(r"ACS_DP5Y2018_pop.csv") # Export df as csv

## Create Percent estimates table for 50 states and DC with NA values less than 25%

### Create percent estimate table
df_PE = df_full.loc[:, df_full.columns.str.contains('PE')] # Select columns by string value
df_PE = df_PE.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_PE["ZCTA"] = df_full["ZCTA"] # save column as separate df

### Susbet for 50 states and DC
df_key = df_key.filter(["ZCTA"]) # Keep only selected columns
df_PE_US = pd.merge(df_key, df_PE, on = "ZCTA", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Drop Duplicates
df_PE_US = df_PE_US.drop_duplicates(subset = "ZCTA", keep = "first", inplace = True) # Drop all dupliacted values

### Drop features with less than 75% data
df_PE_US_NA = df_PE_US.dropna(axis = 1, thresh = 0.75*len(df_PE_US)) # Drop features less than 75% non-NA count for all columns
NAtot = df_PE_US_NA.isnull().sum().sum() # Get count of all NA values
NAnot = df_PE_US_NA.count().sum().sum() # Get count of all nonNA values
NAratio = NAtot / (NAtot + NAnot) # Percent of values with values
print(NAratio) # Print value
df_PE_US_NA.info() # Get info

### Verify 
df_PE_US_NA.info() # Get class, memory, and column info: names, data types, obs.
df_PE_US_NA.head() # Print first 5 observations

### Export full, percent estimate, and label tables
df_PE_US_NA.to_csv(r"ACS_DP5Y2018_PE_US_NA_stage.csv") # Export df as csv

### Write Summary to Text File
text_file = open("ACS_DP5Y2018_PE_US_NA_README.txt", "w") # Open text file and name with subproject, content, and result suffix
text_file.write("American Community Survey 2014-2018 Zip Code Percent Estimates\n") # Title of section with double space after
text_file.write("\nObservations, Features for 50 States and DC\n") # Title of section with double space after
text_file.write(str(df_PE_US.shape)) # write string version of variable above
text_file.write("\n\nSubset with features containing 75% non-missing data\n") # Line of text with space after
text_file.write(str(df_PE_US_NA.shape)) # write string version of variable above
text_file.write("\n\nRatio of NA values to non-NA Values\n") # Line of text with space after
text_file.write(str(NAratio)) # write string version of variable above
text_file.close() # Close file
