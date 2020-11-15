# allocativ
# Healthy Neighborhoods
# Table Join Code Template

## Import Libraries and Data

### Import Python libraries
import os # Operating system navigation

### Import data science libraries
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'

### Set working directory
os.chdir("C:/Users/drewc/GitHub/allocativ/hnb") # Set wd to project repository

### Import datasets from csv files
df_ = pd.read_csv("_data/data.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Modify columns in data frame
df_rename =  df_.rename(columns = {"ColA": "A", "ColB": "B"}) # Rename multiple columns in place

### Merge Join Group in data frame
df_join = pd.merge(df_A, df_B, on = "ColAB", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options



