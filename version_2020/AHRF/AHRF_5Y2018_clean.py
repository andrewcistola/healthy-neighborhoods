# allocativ
# Healthy Neighborhoods
# ACS DP5Y2018 join Code
# Fl ZCTA subset code

## Import Libraries and Data

### Import Python libraries
import os # Operating system navigation

### Import data science libraries
import numpy as np # Widely used matrix library for numerical processes
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'

### Set working directory
os.chdir("C:/Users/drewc/GitHub/allocativ") # Set wd to project repository

## AHRF Clean
df_ahrf = pd.read_csv("hnb/HRSA/AHRF/AHRF_2018_2019_SAS/AHRF_full.csv") # Import dataset saved as csv in _data folder
df_ahrf = df_ahrf.loc[:, df_ahrf.columns.str.contains('2018|2017|2016|2015|2014|FIPS')] # Select columns by string value
df_ahrf = df_ahrf.set_index("FIPS") # Reset Index
df_ahrf = df_ahrf.transpose() # Transpose Rows and Columns
df_ahrf = df_ahrf.reset_index() # Reset Index
df_ahrf['Year'] = df_ahrf['index'].str[-4:]
df_ahrf['index'] = df_ahrf['index'].str.replace(" 2018","") # Strip all spaces from column in data frame
df_ahrf['index'] = df_ahrf['index'].str.replace(" 2017","") # Strip all spaces from column in data frame
df_ahrf['index'] = df_ahrf['index'].str.replace(" 2016","") # Strip all spaces from column in data frame
df_ahrf['index'] = df_ahrf['index'].str.replace(" 2015","") # Strip all spaces from column in data frame
df_ahrf['index'] = df_ahrf['index'].str.replace(" 2014","") # Strip all spaces from column in data frame
df_ahrf = df_ahrf.groupby(["index"], as_index = False).mean() # Group data by columns and average
df_ahrf = df_ahrf.reset_index() # Reset Index
df_ahrf["level_0"] = df_ahrf["level_0"].astype("str") # Change data type of column in data frame
df_ahrf["Code"] = "AHRF" + df_ahrf["level_0"]
df_label = df_ahrf.filter(["Code", "index"]) # Keep only selected columns
df_ahrf = df_ahrf.drop(columns = ["level_0", "index"]) # Drop Unwanted Columns
df_ahrf = df_ahrf.set_index("Code") # Reset Index
df_ahrf = df_ahrf.transpose() # Transpose Rows and Columns
df_ahrf.to_csv(r"hnb/HRSA/AHRF/AHRF_2018_2019_SAS/AHRF_5Y2018_full.csv") # Export df as csv
df_label.to_csv(r"hnb/HRSA/AHRF/AHRF_2018_2019_SAS/AHRF_5Y2018_label.csv") # Export df as csv

