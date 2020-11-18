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
df_1 = pd.read_csv("_data/flcharts_50_stage.csv") # Import dataset from _data folder
df_2 = pd.read_csv("_data/acs_tract_stage.csv", low_memory = False) # Import dataset from _data folder

## Tidy Data Types, Missing Values, and Variable Names

## Verify
df_1.info() # Get class, memory, and column info: names, data types, obs.
df_2.info() # Get class, memory, and column info: names, data types, obs.

### Step 2: Join Datasets

## Join by Tract
df_join = pd.merge(df_1, df_2, on = "Tract", how = "inner")

## Verify
df_join.info() # Get class, memory, and column info: names, data types, obs.

## Export to CSV
df_join.to_csv(r"_data/flcharts_50_acs.csv") # Clean in excel and select variable
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
df_1 = pd.read_csv("_data/flcharts_50_stage.csv") # Import dataset from _data folder
df_2 = pd.read_csv("_data/acs_tract_stage.csv", low_memory = False) # Import dataset from _data folder

## Tidy Data Types, Missing Values, and Variable Names

## Verify
df_1.info() # Get class, memory, and column info: names, data types, obs.
df_2.info() # Get class, memory, and column info: names, data types, obs.

### Step 2: Join Datasets

## Join by Tract
df_join = pd.merge(df_1, df_2, on = "Tract", how = "inner")

## Verify
df_join.info() # Get class, memory, and column info: names, data types, obs.

## Export to CSV
df_join.to_csv(r"_data/flcharts_50_acs.csv") # Clean in excel and select variable
>>>>>>> 321eaea894d29a3f212ee3e111b86695f46cf6db
