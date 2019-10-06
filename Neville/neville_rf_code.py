#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Neville Subproject: Using Random Forestes and Stepwise Regression Modeling to Screen Variables for Improtantance and Relevance
## Base Code Script by DrewC!

### Section 1: Import Libraries, Import Dataset, Prepare for Classification

## Import Libraries
import os # Inlcuded in every script
import numpy as np # Inclduded in every code script
import pandas as pd # Incldued in everycode script
import sklearn.ensemble as sken # SciKit Learn package contains many classification options
from sklearn.ensemble import RandomForestClassifier as rfc # Random Forest classification component

## Import Dataset
os.chdir("C:/Users/drewc/GitHub/HNB") # Set wd to Healthy Neighborhood repository
df_rf = pd.read_csv("_data/rf_dmacs_stage.csv", encoding = "ISO-8859-1") # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository

## Prepare for Classification
df_rf = df_rf.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_rf = df_rf.dropna() # Drop all rows with NA values
df_rf.info() # Verify dataset with info on variables
df_rf.dtypes

### Section 2: Use Random Forest to Classify Ecological Variables by Contribution to Outcome

## Setup Predictors and Forest
features = df_rf.columns.drop(["Tract", "Diabetes"]) # Drop outcome variable and Geo to isolate all predictor variable names as features
X = df_rf[features] # Save features columns as predictor data frame
Y = pd.factorize(df_rf["Diabetes"])[0] # Isolate Outcome variable and factorize as numbers
forest = rfc(n_estimators = 1000, max_depth = 10) #Use default values except for number of trees. For a further explanation see readme included in repository. 

## Run Forest and Output importances
forest.fit(X, Y) # Run fit of predictors and outcome with forest 
gini = forest.feature_importances_ # Output importances of features
l_gini = list(zip(X, gini)) # Create list of variables alongside importance scores 
df_gini = pd.DataFrame(l_gini, columns = ["Variables", "Gini"]) # Create data frame of importances with variables and gini column names
df_gini.info() # Check importance data frame

## Select top variables for passing into regression model
df_gini = df_gini.sort_values(by = ["Gini"], ascending = False) # Sort data frame by gini value in desceding order
df_gini = df_gini.reset_index(drop = True)
df_gini = df_gini.iloc[:100] # Select top 100 variables by Gini coefficient
l_gini = df_gini["Variables"].tolist() # Save variable list
df_forward = df_rf[l_gini]
df_forward.info()
df_forward.info()



### Section 3: Run Stepwise Forwards Mutliple Regression Model

## Recombine with Outcome Data

## Setup for regression model

## Run Regression Model

## Output coefficients

## Print graph of Coefficients of interest