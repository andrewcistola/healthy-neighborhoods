# allocativ
# Healthy Neighborhoods
# State County Zip Key Join Code

## Import Libraries and Data

### Import Python libraries
import os # Operating system navigation

### Import data science libraries
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'

### Set working directory
os.chdir("C:/Users/drewc/GitHub/allocativ/hnb") # Set wd to project repository

### Import datasets from csv files
df_DOH = pd.read_csv("DOH/FL/DeathsReport_5Y2018/FL_113_stage.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_pop = pd.read_csv("ACS/DP5Y2018/ACS_DP5Y2018_pop.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository

### Join with population data from ACS
df_DOH = df_DOH.drop(columns = ["ZIP"]) # Drop Unwanted Columns
df_group = df_DOH.groupby(["ZCTA"], as_index = False).sum() # Group data by columns and sum
df_join = pd.merge(df_group, df_pop, on = "ZCTA", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Verify
df_join.info() # Get class, memory, and column info: names, data types, obs.
df_join.head() # Print first 5 observations

### Write to CSV
df_join.to_csv(r"DOH/FL/DeathsReport_5Y2018/FL_113_rates_stage.csv") # Clean in excel and select variable
