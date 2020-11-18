# allocativ
# Healthy Neighborhoods
# BEA 2018 CAGDP CAINC Join Code

## Import Libraries and Data

### Import Python libraries
import os # Operating system navigation

### Import data science libraries
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'

### Set working directory
os.chdir("C:/Users/drewc/GitHub/allocativ") # Set wd to project repository

### Import datasets from csv files
df_CAGDP1 = pd.read_csv("hnb/BEA/2018/CAGDP1/CAGDP1__ALL_AREAS_2001_2018.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_CAGDP2 = pd.read_csv("hnb/BEA/2018/CAGDP2/CAGDP2__ALL_AREAS_2001_2018.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_CAGDP8 = pd.read_csv("hnb/BEA/2018/CAGDP8/CAGDP8__ALL_AREAS_2001_2018.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_CAGDP9 = pd.read_csv("hnb/BEA/2018/CAGDP9/CAGDP9__ALL_AREAS_2001_2018.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_CAGDP11 = pd.read_csv("hnb/BEA/2018/CAGDP11/CAGDP11__ALL_AREAS_2002_2018.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_CAINC1 = pd.read_csv("hnb/BEA/2018/CAINC1/CAINC1__ALL_AREAS_1969_2018.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_CAINC4 = pd.read_csv("hnb/BEA/2018/CAINC4/CAINC4__ALL_AREAS_1969_2018.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_CAINC30 = pd.read_csv("hnb/BEA/2018/CAINC30/CAINC30__ALL_AREAS_1969_2018.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_key = pd.read_csv("hnb/FIPS/FIPS_ZCTA_key.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

## Combine CAGDP tables

### Stack CAGDP Data Frames
df_stack12 = pd.concat([df_CAGDP1, df_CAGDP2]) # Combine rows with same columns
df_stack128 = pd.concat([df_stack12, df_CAGDP8]) # Combine rows with same columns
df_stack1289 = pd.concat([df_stack128, df_CAGDP9]) # Combine rows with same columns
df_CAGDP = pd.concat([df_stack1289, df_CAGDP11]) # Combine rows with same columns

### Tidy, Rename, and Verify Stacked Data
df_CAGDP.info() # Get class, memory, and column info: names, data types, obs.
df_CAGDP.head() # Print first 5 observations

## Create Feature Label Table

### Pull and clean feature labels
df_label = df_CAGDP.filter(["IndustryClassification", "Description", "Unit", "TableName", "LineCode"]) # Drop Unwanted Columns
df_label['Label'] = df_label['TableName'] + "_" + df_label['LineCode'].astype("str") + "_" + "YEAR" # Combine columns as strings
df_label = df_label.sort_values(by = ["Label"], ascending = False) # Sort Columns by Value
df_label = df_label.drop_duplicates() # Drop all dupliacted values

### Verify
df_label.info() # Get class, memory, and column info: names, data types, obs.
df_label.head() # Print first 5 observations

### Export feature labels
df_label.to_csv(r"hnb/BEA/2018/BEA_2018_CAGDP_label.csv") # Export df as csv

## Prepare CAGDP Data for Joining
df_stack = df_CAGDP # Rename to generic for code portability
df_stack['Label'] = df_stack['TableName'] + "_" + df_stack['LineCode'].astype("str")
df_stack = df_stack.drop(columns = ["GeoName", "Region", "IndustryClassification", "Description", "Unit", "TableName", "LineCode"]) # Drop Unwanted Columns
df_stack = df_stack.dropna() # Drop all rows with NA values
df_long = pd.wide_to_long(df_stack, stubnames = '20', i = ['Label', 'GeoFIPS'], j = 'Year') # Convert from wide to long

### Clean and Convert from Long to Wide
df_long = df_long.reset_index() # Reset Index
df_long['Year'] = '20' + df_long['Year'].astype("str").str.rjust(2, "0") # add leading zeros of character column using rjust() function
df_long['Label'] = df_long['Label'] + "_" + df_long['Year'] # Add strings to columns
df_long = df_long.rename(columns = {"20": "Value"}) # Rename multiple columns in place
df_long["GeoFIPS"] = df_long["GeoFIPS"].str.replace('"',"") # Strip all spaces from column in data frame
df_long["GeoFIPS"] = df_long["GeoFIPS"].str.replace(' ',"") # Strip all spaces from column in data frame
df_long["FIPS"] = "FIPS" + df_long["GeoFIPS"] # Combine columns as string
df_long = df_long.filter(["Label", "Value", "FIPS"]) # Drop Unwanted Columns
df_long["Value"] = df_long["Value"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_long = df_long.dropna() # Drop all rows with NA values
df_long = df_long.pivot_table(index = "FIPS", columns = "Label", values = "Value") # Pivot from Long to Wide Format
df_CAGDP = df_long.reset_index() # Reset Index

### Specify and Verify
df_CAGDP.info() # Get class, memory, and column info: names, data types, obs.
df_CAGDP.head() # Print first 5 observations

### Export full CAGDP table
df_CAGDP.to_csv(r"hnb/BEA/2018/BEA_2018_CAGDP_full.csv") # Export df as csv

## Combine CAINC tables

### Stack CAGDP Data Frames
df_stack14 = pd.concat([df_CAINC1, df_CAINC4]) # Combine rows with same columns
df_CAINC = pd.concat([df_stack14, df_CAINC30]) # Combine rows with same columns

### Tidy, Rename, and Verify Stacked Data
df_CAINC.info() # Get class, memory, and column info: names, data types, obs.
df_CAINC.head() # Print first 5 observations

## Create Feature Label Table

### Pull and clean feature labels
df_label = df_CAINC.filter(["IndustryClassification", "Description", "Unit", "TableName", "LineCode"]) # Drop Unwanted Columns
df_label['Label'] = df_label['TableName'] + "_" + df_label['LineCode'].astype("str") + "_" + "YEAR" # Combine columns as strings
df_label = df_label.sort_values(by = ["Label"], ascending = False) # Sort Columns by Value
df_label = df_label.drop_duplicates() # Drop all dupliacted values

### Verify
df_label.info() # Get class, memory, and column info: names, data types, obs.
df_label.head() # Print first 5 observations

### Export feature labels
df_label.to_csv(r"hnb/BEA/2018/BEA_2018_CAINC_label.csv") # Export df as csv

## Prepare CAINC Data for Joining

### Clean and Convert from Stack to Long
df_stack = df_CAINC # Rename to generic for code portability
df_stack['Label'] = df_stack['TableName'] + "_" + df_stack['LineCode'].astype("str")
df_stack = df_stack.drop(columns = ["GeoName", "Region", "IndustryClassification", "Description", "Unit", "TableName", "LineCode"]) # Drop Unwanted Columns
df_stack = df_stack.dropna() # Drop all rows with NA values
df_long = pd.wide_to_long(df_stack, stubnames = '20', i = ['Label', 'GeoFIPS'], j = 'Year') # Convert from wide to long

### Clean and Convert from Long to Wide
df_long = df_long.reset_index() # Reset Index
df_long['Year'] = '20' + df_long['Year'].astype("str").str.rjust(2, "0") # add leading zeros of character column using rjust() function
df_long['Label'] = df_long['Label'] + "_" + df_long['Year'] # Add strings to columns
df_long = df_long.rename(columns = {"20": "Value"}) # Rename multiple columns in place
df_long["GeoFIPS"] = df_long["GeoFIPS"].str.replace('"',"") # Strip all spaces from column in data frame
df_long["GeoFIPS"] = df_long["GeoFIPS"].str.replace(' ',"") # Strip all spaces from column in data frame
df_long["FIPS"] = "FIPS" + df_long["GeoFIPS"] # Combine columns as string
df_long = df_long.filter(["Label", "Value", "FIPS"]) # Drop Unwanted Columns
df_long["Value"] = df_long["Value"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_long = df_long.dropna() # Drop all rows with NA values
df_long = df_long.pivot_table(index = "FIPS", columns = "Label", values = "Value") # Pivot from Long to Wide Format
df_CAINC = df_long.reset_index() # Reset Index

### Specify and Verify
df_CAINC.info() # Get class, memory, and column info: names, data types, obs.
df_CAINC.head() # Print first 5 observations

### Export full CAGDP table
df_CAINC.to_csv(r"hnb/BEA/2018/BEA_2018_CAINC_full.csv") # Export df as csv

## Create full BEA table and stage

### Join CAGDP CAINC
df_join = pd.merge(df_CAINC, df_CAGDP, on = "FIPS", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options
df_index = df_join.set_index("FIPS") # Set column as index

### Subset for 2010 and later
df_2010 = df_index.loc[:, df_index.columns.str.contains('201')] # Select columns by string value, subset for 2010 census boundaires

### Join with FIPS key to susbet by 50 states and get population estimate
df_group = df_key.groupby(["FIPS"], as_index = False).sum() # Group data by columns and count
df_50 = pd.merge(df_2010, df_group, on = "FIPS", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Drop features with less than 75% data
df_NA = df_50.dropna(axis = 1, thresh = 0.75*len(df_50)) # Drop features less than 75% non-NA count for all columns
NAtot = df_NA.isnull().sum().sum() # Get count of all NA values
NAnot = df_NA.count().sum().sum() # Get count of all nonNA values
NAratio = NAtot / (NAtot + NAnot) # Percent of values with values
print(NAratio) # Print value
df_NA.info() # Get info

### Rename and Verify 
df_BEA = df_NA # Rename data frame
df_BEA.info() # Get class, memory, and column info: names, data types, obs.
df_BEA.head() # Print first 5 observations

### Export full, percent estimate, and label tables
df_BEA.to_csv(r"BEA/2018/BEA_2018_CAGDP_CAINC_2010_50_NA.csv") # Export df as csv

### Write Summary to Text File
text_file = open("hnb/BEA/2018/BEA_2018_CAGDP_CAINC_2010_50_NA_README.txt", "w") # Open text file and name with subproject, content, and result suffix
text_file.write("Beureau of Economic Analysis County Equivalent Tables 2010-2018\n") # Title of section with double space after
text_file.write("\nObservations, Features for 50 States and DC\n") # Title of section with double space after
text_file.write(str(df_50.shape)) # write string version of variable above
text_file.write("\n\nSubset with features containing 75% non-missing data\n") # Line of text with space after
text_file.write(str(df_NA.shape)) # write string version of variable above
text_file.write("\n\nRatio of NA values to non-NA Values\n") # Line of text with space after
text_file.write(str(NAratio)) # write string version of variable above
text_file.close() # Close file




