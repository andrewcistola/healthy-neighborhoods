# allocativ
# Healthy Neighborhoods
# CMS Hospital Compare 2018 and 2019

## Import Libraries and Data

### Import Python libraries
import os # Operating system navigation
import sqlite3 # SQLite database manager

### Import data science libraries
import numpy as np # Widely used matrix library for numerical processes
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'

### Set working directory
os.chdir("C:/Users/drewc/GitHub/allocativ") # Set wd to project repository

## Create Facility ID table from Hosptial General Information

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HC/Hospital General Information.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_key = pd.read_csv("hnb/FIPS/FIPS_ZCTA_key.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository

### Save Hospital ID key
df_id = df_raw.filter(['Facility ID', 'Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Phone Number', 'Hospital Type', 'Hospital Ownership'])
df_id = df_id.rename(columns = {"ZIP Code": "ZIP"}) # Rename multiple columns in place
df_key = df_key.filter(["ZIP", "FIPS", "ZCTA"]) # Keep only selected columns
df_id = pd.merge(df_id, df_key, on = "ZIP", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Rename and Veirfy
df_id.info() # Get class, memory, and column info: names, data types, obs.
df_id.head() # Print first 5 observations

### Export facility id csv
df_id.to_csv(r"hnb/CMS/CMS_2018_id.csv") # Export df as csv

## Conenct Hospital to Area File

### Import Datasets
df_area = pd.read_csv("_dev/allocativ/hnb_14-11-2020/release_2020/CMS/AREA/Hospital_Service_Area_File_-_2018.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository

### Subset by Zip Codes with Inpatient visits
df_area = df_area[df_area["TOTAL_DAYS_OF_CARE"] > 0] # Susbet numeric column by condition
df_area = df_area.filter(["ZIP_CODE", "MEDICARE_PROV_NUM"]) # Keep only selected columns
df_area = df_area.rename(columns = {"ZIP_CODE": "ZIP", "MEDICARE_PROV_NUM": "Provider ID"}) # Rename multiple columns in place



### Convert numeric to character
df_area['ZIP'] = df_area['ZIP'].astype("str") # Change data type of column in data frame
df_area['ZIP'] = df_area['ZIP'].str.rjust(5, "0") # add leading zeros of character column using rjust() function
df_area["ZCTA"] = "ZCTA"+ df_area['ZIP'] # Combine string with column
df_area = df_area.drop(columns = ["ZIP"]) # Drop Unwanted Columns

### Export facility id csv
df_area.to_csv(r"hnb/CMS/CMS_2018_area.csv") # Export df as csv

### Export facility id to SQLite database
df_id.to_sql('CMS_2018_Facility_ID', con = sqlite3.connect('hnb/_database/HNB.db'), if_exists = 'replace', index = False)

############## 19 Oct 2020 HSAF Redo

df_hsaf = pd.read_csv("_dev/allocativ/hnb_14-11-2020/release_2020/CMS/AREA/Hospital_Service_Area_File_-_2018.csv") # Import dataset saved as csv in _data folder
df_hsaf = df_hsaf.drop(columns = ["MEDICARE_PROV_NUM"]) # Drop Unwanted Columns
df_hsaf = df_hsaf.groupby(["ZIP_CODE"], as_index = False).sum() # Group data by columns and sum
df_hsaf.head()

df_hsaf['ZCTA'] = df_hsaf['ZIP_CODE'].astype("int64") # Change data type of column in data frame
df_hsaf['ZCTA'] = df_hsaf['ZCTA'].astype("str") # Change data type of column in data frame
df_hsaf['ZCTA'] = df_hsaf['ZCTA'].str.rjust(5, "0") # add leading zeros of character column using rjust() function
df_hsaf["ZCTA"] = "ZCTA"+ df_hsaf['ZCTA'] # Combine string with column
df_hsaf = df_hsaf.drop(columns = ["ZIP_CODE"]) # Drop Unwanted Columns
df_hsaf.head()

df_pop = pd.read_csv("_dev/allocativ/hnb_14-11-2020/release_2020/ACS/ACS_DP5Y2018_ZCTA_full.csv") # Import dataset saved as csv in _data folder
df_pop = df_pop.filter(["DP05_0029PE", "ZCTA"]) # Rename data frame
df_pop =  df_pop.rename(columns = {"DP05_0029PE": "POP_OVER_65"}) # Rename multiple columns in place
df_hsaf = pd.merge(df_pop, df_hsaf, on = "ZCTA", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options
df_hsaf.head()

df_hsaf = df_hsaf[df_hsaf['TOTAL_CASES'] > 50] # Susbet numeric column by condition
df_hsaf = df_hsaf[df_hsaf['POP_OVER_65'] > 100] # Susbet numeric column by condition

df_hsaf["DAYS_per65"] = df_hsaf['TOTAL_DAYS_OF_CARE'] / df_hsaf["POP_OVER_65"] # Combine string with column
df_hsaf["CHARGES_per65"] = df_hsaf['TOTAL_CHARGES'] / df_hsaf["POP_OVER_65"] # Combine string with column
df_hsaf["VISITS_per65"] = df_hsaf['TOTAL_CASES'] / df_hsaf["POP_OVER_65"] # Combine string with column
df_hsaf.head()

df_hsaf.info() # Get class, memory, and column info: names, data types, obs.

df_hsaf.to_csv(r"_dev/allocativ/hnb_14-11-2020/release_2020/CMS/ffs_2018_ZCTA.csv") # Export df as csv



##############




## Clean Hospital General Info

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HC/Hospital General Information.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_clean = df_raw.drop(columns = ['Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Phone Number', 'Hospital Type'])

### Remove and footnote items
df_clean = df_clean.loc[:, ~df_clean.columns.str.contains('footnote')] # Select columns by string value, subset for 2010 census boundaires

### Create binary outcomes from general info
df_clean["Meets criteria for promoting interoperability of EHRs"] = np.where(df_clean["Meets criteria for promoting interoperability of EHRs"] == "Y", 1, 0) # Create New Column Based on Conditions
df_clean["Emergency Services"] = np.where(df_clean["Emergency Services"] == "Yes", 1, 0) # Create New Column Based on Conditions
df_clean["Hospital Ownership NonProfit"] = np.where(df_clean["Hospital Ownership"].str.contains("Voluntary non-profit"), 1, 0) # Create New Column Based on Conditions
df_clean["Hospital Ownership ForProfit"] = np.where(df_clean["Hospital Ownership"].str.contains("Proprietary"), 1, 0) # Create New Column Based on Conditions
df_clean["Hospital Ownership Public"] = np.where(df_clean["Hospital Ownership"].str.contains("Government"), 1, 0) # Create New Column Based on Conditions
df_clean = df_clean.drop(columns = ["Hospital Ownership", "Emergency Services", "Meets criteria for promoting interoperability of EHRs"]) # Drop Unwanted Columns
df_gen = df_clean.loc[:, ~df_clean.columns.str.contains('comparison')] # Select columns by string value, subset for 2010 census boundaires

### Create below average binary outcomes from comparison data
df_below = df_clean.drop(columns = ["Hospital overall rating", "Hospital Ownership NonProfit", "Hospital Ownership ForProfit", "Hospital Ownership Public"]) # Drop Unwanted Columns
df_below.loc[:, df_below.columns.str.contains('comparison')] = np.where(df_below.loc[:, df_below.columns.str.contains('comparison')] == "Below the national average", 1, 0) # Create New Column Based on Conditions
df_below = df_below.set_index("Facility ID") # Set column as index
df_below = df_below.add_suffix(' Below Average') # Add suffix to column names
df_below = df_below.reset_index() # Reset Index

### Create above average binary outcomes from comparison data
df_above = df_clean.drop(columns = ["Hospital overall rating", "Hospital Ownership NonProfit", "Hospital Ownership ForProfit", "Hospital Ownership Public"]) # Drop Unwanted Columns
df_above.loc[:, df_above.columns.str.contains('comparison')] = np.where(df_above.loc[:, df_above.columns.str.contains('comparison')] == "Above the national average", 1, 0) # Create New Column Based on Conditions
df_above = df_above.set_index("Facility ID") # Set column as index
df_above = df_above.add_suffix(' Above Average') # Add suffix to column names
df_above = df_above.reset_index() # Reset Index

### Join general, above average, and below average dataframes
df_clean = pd.merge(df_above, df_below, on = "Facility ID", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options
df_clean = pd.merge(df_gen, df_clean, on = "Facility ID", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Clean data types and missing values
df_clean = df_clean.set_index("Facility ID") # Set column as index
df_clean = df_clean.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_clean = df_clean.fillna(0).astype(np.int64) # Remove NA and change to int64 zeros
df_clean = df_clean.reset_index() # Reset Index

### Rename and Veirfy
df_comp = df_clean
df_comp.info() # Get class, memory, and column info: names, data types, obs.
df_comp.head() # Print first 5 observations

## Structural Measures

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HC/Structural Measures - Hospital.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_score = df_raw.drop(columns = ['Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Phone Number']) # Drop General info

### Clean score data and create binary outcomes
df_score = df_score.drop(columns = ['Measure Name', 'Footnote', 'Start Date', 'End Date']) # Remove Single score info
df_score["Receive Electronic Labs"] = np.where((df_score["Measure ID"] == "OP_12") & (df_score["Measure Response"] == "Yes"), 1, 0) # Create New Column Based on Conditions
df_score["Track Electronic Labs"] = np.where((df_score["Measure ID"] == "OP_17") & (df_score["Measure Response"] == "Yes"), 1, 0) # Create New Column Based on Conditions
df_score = df_score.drop(columns = ['Measure ID', 'Measure Response']) # Remove Single score info
df_score = df_score.groupby(["Facility ID"], as_index = False).sum() # Group data by columns and sum

### Clean data types and missing values
df_score = df_score.set_index("Facility ID") # Set column as index
df_score = df_score.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_score = df_score.fillna(0).astype(np.int64) # Remove NA and change to int64 zeros
df_score = df_score.reset_index() # Reset Index
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame

### Rename and Veirfy
df_lab = df_score
df_lab.info() # Get class, memory, and column info: names, data types, obs.
df_lab.head() # Print first 5 observations

## Imaging Scores

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HC/Outpatient Imaging Efficiency - Hospital.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_score = df_raw.drop(columns = ['Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Phone Number']) # Drop General info

### Clean score data and create binary outcomes
df_score = df_score.drop(columns = ['Measure ID', 'Footnote', 'Start Date', 'End Date']) # Remove Single score info
df_score["Score"] = df_score["Score"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_score = df_score.pivot_table(index = "Facility ID", columns = "Measure Name", values = "Score") # Pivot from Long to Wide Format
df_score = df_score.reset_index() # Reset Index

### Clean data types and missing values
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame

### Rename and Veirfy
df_img = df_score
df_img.info() # Get class, memory, and column info: names, data types, obs.
df_img.head() # Print first 5 observations

## Complications and Deaths

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HC/Complications and Deaths - Hospital.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_score = df_raw.drop(columns = ['Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Phone Number']) # Drop General info

### Clean score data and create binary outcomes
df_score = df_score.filter(['Facility ID', 'Measure Name', 'Score']) # Remove Single score info
df_score["Score"] = df_score["Score"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_score = df_score.pivot_table(index = "Facility ID", columns = "Measure Name", values = "Score") # Pivot from Long to Wide Format
df_score = df_score.reset_index() # Reset Index

### Clean data types and missing values
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame

### Rename and Veirfy
df_dth = df_score
df_dth.info() # Get class, memory, and column info: names, data types, obs.
df_dth.head() # Print first 5 observations

## Annual Hospital Patient Survey

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HC/HCAHPS - Hospital.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_score = df_raw.drop(columns = ['Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Phone Number']) # Drop General info

### Clean score data and create binary outcomes
df_score = df_score.filter(['Facility ID', 'HCAHPS Question', 'HCAHPS Answer Percent']) # Remove Single score info
df_score["HCAHPS Answer Percent"] = df_score["HCAHPS Answer Percent"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_score = df_score.pivot_table(index = "Facility ID", columns = "HCAHPS Question", values = "HCAHPS Answer Percent") # Pivot from Long to Wide Format
df_score = df_score.reset_index() # Reset Index

### Clean data types and missing values
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame

### Rename and Veirfy
df_ahps = df_score
df_ahps.info() # Get class, memory, and column info: names, data types, obs.
df_ahps.head() # Print first 5 observations

## Hospital Acquired Infections

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HC/Healthcare Associated Infections - Hospital.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_score = df_raw.drop(columns = ['Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Phone Number']) # Drop General info

### Clean score data and create binary outcomes
df_score = df_score.filter(['Facility ID', 'Measure Name', 'Score', 'Measure ID']) # Remove Single score info
df_score = df_score[df_score["Measure ID"].str.contains("SIR")] # Subset character column by string
df_score = df_score.drop(columns = ['Measure ID']) # Drop General info
df_score["Score"] = df_score["Score"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_score = df_score.pivot_table(index = "Facility ID", columns = "Measure Name", values = "Score") # Pivot from Long to Wide Format
df_score = df_score.reset_index() # Reset Index

### Clean data types and missing values
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame

### Rename and Veirfy
df_hac = df_score
df_hac.info() # Get class, memory, and column info: names, data types, obs.
df_hac.head() # Print first 5 observations

## MSPB

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HC/Medicare Hospital Spending Per Patient - Hospital.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_score = df_raw.drop(columns = ['Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Phone Number']) # Drop General info

### Clean score data and create binary outcomes
df_score = df_score.filter(['Facility ID', 'Measure Name', 'Score']) # Remove Single score info
df_score["Score"] = df_score["Score"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_score = df_score.pivot_table(index = "Facility ID", columns = "Measure Name", values = "Score") # Pivot from Long to Wide Format
df_score = df_score.reset_index() # Reset Index

### Clean data types and missing values
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame

### Rename and Veirfy
df_mspb = df_score
df_mspb.info() # Get class, memory, and column info: names, data types, obs.
df_mspb.head() # Print first 5 observations

## Payment

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HC/Payment and Value of Care - Hospital.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_score = df_raw.drop(columns = ['Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Phone Number']) # Drop General info

### Clean score data and create binary outcomes
df_score = df_score.filter(['Facility ID', 'Payment Measure Name', 'Payment']) # Remove Single score info
df_score['Payment'] = df_score['Payment'].str.replace("$","") # Strip all spaces from column in data frame
df_score['Payment'] = df_score['Payment'].str.replace(",","") # Strip all spaces from column in data frame
df_score['Payment'] = df_score['Payment'].str.replace(" ","") # Strip all spaces from column in data frame
df_score["Payment"] = df_score["Payment"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_score = df_score.pivot_table(index = "Facility ID", columns = "Payment Measure Name", values = "Payment") # Pivot from Long to Wide Format
df_score = df_score.reset_index() # Reset Index

### Clean data types and missing values
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame

### Rename and Veirfy
df_pay = df_score
df_pay.info() # Get class, memory, and column info: names, data types, obs.
df_pay.head() # Print first 5 observations

## Timely

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HC/Timely and Effective Care - Hospital.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_score = df_raw.drop(columns = ['Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Phone Number']) # Drop General info

### Clean score data and create binary outcomes
df_score = df_score.filter(['Facility ID', 'Measure Name', 'Score']) # Remove Single score info
df_score["Score"] = df_score["Score"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_score = df_score.pivot_table(index = "Facility ID", columns = "Measure Name", values = "Score") # Pivot from Long to Wide Format
df_score = df_score.reset_index() # Reset Index

### Clean data types and missing values
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame

### Rename and Veirfy
df_time = df_score
df_time.info() # Get class, memory, and column info: names, data types, obs.
df_time.head() # Print first 5 observations

## ED volume

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HC/Timely and Effective Care - Hospital.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_score = df_raw.drop(columns = ['Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Phone Number']) # Drop General info

### Clean score data and create binary outcomes
df_score = df_score.filter(['Facility ID', 'Measure Name', 'Score']) # Remove Single score info
df_score["Emergency department volumn very high"] = np.where((df_score["Measure Name"] == "Emergency department volume") & (df_score["Score"] == "very high"), 1, 0) # Create New Column Based on Conditions
df_score["Emergency department volumn high"] = np.where((df_score["Measure Name"] == "Emergency department volume") & (df_score["Score"] == "high"), 1, 0) # Create New Column Based on Conditions
df_score["Emergency department volumn medium"] = np.where((df_score["Measure Name"] == "Emergency department volume") & (df_score["Score"] == "medium"), 1, 0) # Create New Column Based on Conditions
df_score["Emergency department volumn low"] = np.where((df_score["Measure Name"] == "Emergency department volume") & (df_score["Score"] == "low"), 1, 0) # Create New Column Based on Conditions
df_score = df_score.drop(columns = ['Measure Name', 'Score']) # Remove Single score info

### Clean data types and missing values
df_score = df_score.set_index("Facility ID") # Set column as index
df_score = df_score.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_score = df_score.fillna(0).astype(np.int64) # Remove NA and change to int64 zeros
df_score = df_score.reset_index() # Reset Index
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame
df_score = df_score.groupby(["Facility ID"], as_index = False).sum() # Group data by columns and sum

### Rename and Veirfy
df_ed = df_score
df_ed.info() # Get class, memory, and column info: names, data types, obs.
df_ed.head() # Print first 5 observations

## Unplanned Visits

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HC/Unplanned Hospital Visits - Hospital.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_score = df_raw.drop(columns = ['Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Phone Number']) # Drop General info

### Clean score data and create binary outcomes
df_score = df_score.filter(['Facility ID', 'Measure Name', 'Score']) # Remove Single score info
df_score["Score"] = df_score["Score"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_score = df_score.pivot_table(index = "Facility ID", columns = "Measure Name", values = "Score") # Pivot from Long to Wide Format
df_score = df_score.reset_index() # Reset Index

### Clean data types and missing values
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame

### Rename and Veirfy
df_un = df_score
df_un.info() # Get class, memory, and column info: names, data types, obs.
df_un.head() # Print first 5 observations

## VBHC Scores

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/VBHC/Hospital_Value-Based_Purchasing__HVBP____Total_Performance_Score.csv") # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_score = df_raw.drop(columns = ['Facility Name', 'Address', 'City', 'State', 'ZIP Code', 'County Name', 'Location']) # Drop General info

### Clean score data and create outcomes
df_score = df_score.loc[:, ~df_score.columns.str.contains('Unweighted')] # Select columns by string value, subset for 2010 census boundaires

### Clean data types and missing values
df_score = df_score.set_index("Facility ID") # Set column as index
df_score = df_score.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_score = df_score.fillna(0).astype(np.int64) # Remove NA and change to int64 zeros
df_score = df_score.reset_index() # Reset Index
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame

### Rename and Veirfy
df_vbhc = df_score
df_vbhc.info() # Get class, memory, and column info: names, data types, obs.
df_vbhc.head() # Print first 5 observations

## HAC Scores

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HAC/Hospital-Acquired_Condition_Reduction_Program.csv") # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository

### Clean score data and create outcomes
df_score = df_raw.filter(['Facility ID', 'TOTAL HAC SCORE']) # Remove Single score info

### Clean data types and missing values
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame

### Rename and Veirfy
df_hacs = df_score
df_hacs.info() # Get class, memory, and column info: names, data types, obs.
df_hacs.head() # Print first 5 observations

## HRR Scores

### Import Datasets
df_raw = pd.read_csv("hnb/CMS/HRR/Hospital_Readmissions_Reduction_Program.csv") # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository

### Clean score data and create binary outcomes
df_score = df_raw.filter(['Facility ID', 'Measure Name', 'Excess Readmission Ratio']) # Remove Single score info
df_score["Excess Readmission Ratio"] = df_score["Excess Readmission Ratio"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_score = df_score.pivot_table(index = "Facility ID", columns = "Measure Name", values = "Excess Readmission Ratio") # Pivot from Long to Wide Format
df_score = df_score.reset_index() # Reset Index

### Clean data types and missing values
df_score['Facility ID'] = df_score['Facility ID'].astype("str") # Change data type of column in data frame

### Rename and Veirfy
df_hrr = df_score
df_hrr.info() # Get class, memory, and column info: names, data types, obs.
df_hrr.head() # Print first 5 observations

## Join CMS Measures into single table

### Join Outcome tables
df_join = pd.merge(df_comp, df_lab, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = pd.merge(df_img, df_join, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = pd.merge(df_dth, df_join, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = pd.merge(df_ahps, df_join, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = pd.merge(df_hac, df_join, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = pd.merge(df_mspb, df_join, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = pd.merge(df_pay, df_join, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = pd.merge(df_time, df_join, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = pd.merge(df_ed, df_join, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = pd.merge(df_un, df_join, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = pd.merge(df_vbhc, df_join, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = pd.merge(df_hacs, df_join, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join = pd.merge(df_hrr, df_join, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options

### Rename and Veirfy
df_hc = df_join
df_hc.info() # Get class, memory, and column info: names, data types, obs.
df_hc.head() # Print first 5 observations

### Export facility id csv
df_hc.to_csv(r"hnb/CMS/CMS_2018_hc.csv") # Export df as csv

### Export facility id to SQLite database
df_hc.to_sql('CMS_2018_hc', con = sqlite3.connect('hnb/_database/HNB.db'), if_exists = 'replace', index = False)

## Final Adjusted Payment

### Import Datasets
df_18 = pd.read_csv("hnb/CMS/ADJ/2018/FY2018_Table16B_19Sep2017.csv") # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_19 = pd.read_csv("hnb/CMS/ADJ/2019/FY2019_Table16B_24Sep2018.csv") # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_20 = pd.read_csv("hnb/CMS/ADJ/2020/Hospital VBP FY2020_Table16B_16Sep2019.csv") # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository

### CLean extra columns
df_18 = df_18.filter(['Facility ID', '2018 VBP Adjustment Factor']) # Remove Single score info
df_19 = df_19.filter(['Facility ID', '2019 VBP Adjustment Factor']) # Remove Single score info
df_20 = df_20.filter(['Facility ID', '2020 VBP Adjustment Factor']) # Remove Single score info

### Clean data types and missing values
df_18['Facility ID'] = df_18['Facility ID'].astype("str") # Change data type of column in data frame
df_19['Facility ID'] = df_19['Facility ID'].astype("str") # Change data type of column in data frame
df_20['Facility ID'] = df_20['Facility ID'].astype("str") # Change data type of column in data frame

### Join Data
df_adj = pd.merge(df_18, df_19, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options
df_adj = pd.merge(df_adj, df_20, on = "Facility ID", how = "outer") # Join by column while keeping only items that exist in both, select outer or left for other options

### Verify
df_adj.info() # Get class, memory, and column info: names, data types, obs.
df_adj.head() # Print first 5 observations

### Export facility id csv
df_adj.to_csv(r"hnb/CMS/CMS_adj.csv") # Export df as csv

### Export facility id to SQLite database
df_adj.to_sql('CMS_adj', con = sqlite3.connect('hnb/_database/HNB.db'), if_exists = 'replace', index = False)

## Combine adjustments, hc, and key

### Import datasets
df_hc = pd.read_csv("hnb/CMS/CMS_2018_hc.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_hc['Facility ID'] = df_hc['Facility ID'].astype("str") # Change data type of column in data frame
df_adj = pd.read_csv("hnb/CMS/CMS_2018_adj.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_adj['Facility ID'] = df_adj['Facility ID'].astype("str") # Change data type of column in data frame

### Join hospital compare and adjusted payment datasets
df_join = pd.merge(df_adj, df_hc, on = "Facility ID", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Join CMS and FIPS
df_id = df_id.filter(["Facility ID", "FIPS"]) # Keep only selected columns
df_join = pd.merge(df_id, df_join, on = "Facility ID", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Verify
df_CMS = df_join
df_CMS.info() # Get class, memory, and column info: names, data types, obs.
df_CMS.head() # Print first 5 observations

### Export facility id csv
df_CMS.to_csv(r"hnb/CMS/CMS_2018_FIPS_full.csv") # Export df as csv

### Export facility id to SQLite database
df_CMS.to_sql('CMS_2018_FIPS_full', con = sqlite3.connect('hnb/_database/HNB.db'), if_exists = 'replace', index = False)

### Add FIPS to Adjustment Table
df_id = pd.read_csv("hnb/CMS/CMS_2018_id.csv", encoding = "ISO-8859-1", low_memory = False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_id = df_id.filter(["Facility ID", "FIPS"]) # Keep only selected columns
df_adj = pd.read_csv("hnb/CMS/CMS_2018_adj.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_adj['Facility ID'] = df_adj['Facility ID'].astype("str") # Change data type of column in data frame
df_join = pd.merge(df_id, df_adj, on = "Facility ID", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join.info()
df_join.to_csv(r"hnb/CMS/CMS_FIPS_adj.csv") # Export df as csv

## Labels
df_ = pd.read_csv("hnb/CMS/CMS_2018_FIPS_full.csv") # Import dataset saved as csv in _data folder
df_ = df_.set_index("Facility ID") # Reset Index
df_ = df_.transpose() # Transpose Rows and Columns
df_ = df_.reset_index() # Reset Index
df_ = df_.reset_index() # Reset Index
df_["level_0"] = df_["level_0"].astype("str") # Change data type of column in data frame
df_["Code"] = "CMS_2018_" + df_["level_0"]
df_lab = pd.DataFrame()
df_lab["index"] = df_["index"] # Keep only selected columns
df_lab["Code"] = df_["Code"] # Keep only selected columns
df_ = df_.set_index("Code") # Reset Index
df_ = df_.drop(columns = ["level_0", "index"]) # Drop Unwanted Columns
df_ = df_.transpose() # Transpose Rows and Columns
df_ = df_.reset_index() # Reset Index
df_["Facility ID"] = df_["Facility ID"].astype("str") # Change data type of column in data frame
df_id = pd.read_csv("hnb/CMS/CMS_2018_id.csv", encoding = "ISO-8859-1", low_memory = False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository
df_id = df_id.filter(["Facility ID", "FIPS", "State"]) # Keep only selected columns
df_id["Facility ID"] = df_id["Facility ID"].astype("str") # Change data type of column in data frame
df_ = pd.merge(df_id, df_, on = "Facility ID", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options
df_.to_csv(r"hnb/CMS/CMS_2018_FIPS_code.csv") # Export df as csv
df_lab.to_csv(r"hnb/CMS/CMS_2018_FIPS_label.csv") # Export df as csv
