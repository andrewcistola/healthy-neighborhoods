#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Mungos subproject: Evaluating Hospital quality and value data
## CMS Hospital Readmission and MCPB for Medicare: Pyhton Computing Language Code Script by DrewC!

### Section 1: Import Libraries, Import Dataset, Tidy Data

## Import Standard Libraries
import os # Inlcuded in every script DC!
import pandas as pd # Incldued in every code script for DC!
import numpy as np # Inclduded in every code script DC!
import scipy as sp  # Incldued in every code script for DC!

## Import Datasets
os.chdir("C:/Users/drewc/GitHub/HNB") # Set wd to project repository
df_gen = pd.read_csv("_data/cms_hosp_gen_stage.csv") # Import dataset from _data folder
df_re = pd.read_csv("_data/cms_hosp_readmit_stage.csv") # Import dataset from _data folder
df_ms = pd.read_csv("_data/cms_hosp_mspb_stage.csv") # Import dataset from _data folder

## Tidy Data Types, Missing Values, and Variable Names
df_re["ERR"] = df_re["ERR"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric

## Verify
df_gen.info() # Get class, memory, and column info: names, data types, obs.
df_re.info() # Get class, memory, and column info: names, data types, obs.
df_ms.info() # Get class, memory, and column info: names, data types, obs.

### Step 2: ERR Data

## Join ERR and General Hospital Data
df_ra = pd.merge(df_gen, df_re, on = "FacilityID", how = "right")

## Subset by Florida and Myocardial Infarction
df_np = df_ra[(df_ra["Ownership"].str.contains("Voluntary", na = False))]
df_fl = df_np[(df_np["State"].str.contains("FL", na = False))]
df_co = df_fl.groupby(["County"], as_index = False).mean() #### Group data By Columns and Sum
df_err = df_co.drop(columns = ["FacilityID", "ZIP"]) # Drop Unwanted Columns

## Verify
df_err.info()
df_err.head()

### Step 3: MSPB Data

## Join ERR and General Hospital Data
df_pb = pd.merge(df_gen, df_ms, on = "FacilityID", how = "inner")

## Subset by Florida and Non-Profit
df_np = df_pb[(df_pb["Ownership"].str.contains("Voluntary", na = False))]
df_fl = df_np[(df_np["State"].str.contains("FL", na = False))]

## Group by COunty and Clean
df_co = df_fl.groupby(["County"], as_index = False).mean() #### Group data By Columns and Sum
df_mspb = df_co.drop(columns = ["FacilityID", "ZIP"]) # Drop Unwanted Columns

## Verify
df_mspb.info()
df_mspb.head()

### Step 4: Join

## Join
df_value = pd.merge(df_err, df_mspb, on = "County", how = "inner")

## Export
df_value.to_csv(r"_data/mungos_np_value.csv") # Clean in excel and select variable