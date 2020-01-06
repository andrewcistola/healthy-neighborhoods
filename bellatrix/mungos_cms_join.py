<<<<<<< HEAD
#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Cedric subproject: Developing better ways to measure equity in health using the Gini coefficient
## Florida Charts Census Tract Mortality Data:  Pyhton Computing Language Code Script by DrewC!

### Step 1: Import Libraries and Import Dataset

## Import Standard Libraries
import os # Inlcuded in every script DC!
import pandas as pd # Incldued in every code script for DC!
import numpy as np # Inclduded in every code script DC!
import scipy as sp  # Incldued in every code script for DC!

## Import Datasets
os.chdir("C:/Users/drewc/GitHub/HNB") # Set wd to project repository
df_1 = pd.read_csv("_data/cms_hosp_gen_stage.csv") # Import dataset from _data folder
df_2 = pd.read_csv("_data/cms_hosp_mspb_stage.csv") # Import dataset from _data folder
df_3 = pd.read_csv("_data/cms_hosp_readmit_stage.csv") # Import dataset from _data folder

## Tidy Data Types, Missing Values, and Variable Names
df_2["MSPB"] = df_2["MSPB"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_3["ERR"] = df_3["ERR"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric

## Verify
df_1.info() # Get class, memory, and column info: names, data types, obs.
df_2.info() # Get class, memory, and column info: names, data types, obs.
df_3.info() # Get class, memory, and column info: names, data types, obs.

### Step 2: Join Datasets

## Join by Column
df_join = pd.merge(df_1, df_2, on = "FacilityID", how = "inner")
df_join2 = pd.merge(df_1, df_3, on = "FacilityID", how = "right")

## Export to CSV
df_join.to_csv(r"_data/cms_hosp_gen_mspb.csv") # Clean in excel and select variable
=======
#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Cedric subproject: Developing better ways to measure equity in health using the Gini coefficient
## Florida Charts Census Tract Mortality Data:  Pyhton Computing Language Code Script by DrewC!

### Step 1: Import Libraries and Import Dataset

## Import Standard Libraries
import os # Inlcuded in every script DC!
import pandas as pd # Incldued in every code script for DC!
import numpy as np # Inclduded in every code script DC!
import scipy as sp  # Incldued in every code script for DC!

## Import Datasets
os.chdir("C:/Users/drewc/GitHub/HNB") # Set wd to project repository
df_1 = pd.read_csv("_data/cms_hosp_gen_stage.csv") # Import dataset from _data folder
df_2 = pd.read_csv("_data/cms_hosp_mspb_stage.csv") # Import dataset from _data folder
df_3 = pd.read_csv("_data/cms_hosp_readmit_stage.csv") # Import dataset from _data folder

## Tidy Data Types, Missing Values, and Variable Names
df_2["MSPB"] = df_2["MSPB"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_3["ERR"] = df_3["ERR"].apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric

## Verify
df_1.info() # Get class, memory, and column info: names, data types, obs.
df_2.info() # Get class, memory, and column info: names, data types, obs.
df_3.info() # Get class, memory, and column info: names, data types, obs.

### Step 2: Join Datasets

## Join by Column
df_join = pd.merge(df_1, df_2, on = "FacilityID", how = "inner")
df_join2 = pd.merge(df_1, df_3, on = "FacilityID", how = "right")

## Export to CSV
df_join.to_csv(r"_data/cms_hosp_gen_mspb.csv") # Clean in excel and select variable
>>>>>>> 321eaea894d29a3f212ee3e111b86695f46cf6db
df_join2.to_csv(r"_data/cms_hosp_gen_readmit.csv") # Clean in excel and select variable