#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Neville Subproject: Using Random Forestes and Stepwise Regression Modeling to Screen Variables for Improtantance and Relevance
## County Level US data: Base Code Script by DrewC!

### Section 1: Import Libraries, Import Dataset, Prepare for Classification

## Import Standard Libraries
import os # Inlcuded in every script DC!
import numpy as np # Inclduded in every code script DC!
import pandas as pd # Incldued in every code script for DC!

## Import Machine Learning Libraries
import sklearn.ensemble # SciKit Learn package contains many classification options beyond those used below
from sklearn.ensemble import RandomForestClassifier as rfc # Random Forest classification component
from sklearn.feature_selection import RFE as rfe # Recursive Feature selection component
from sklearn.svm import SVR as svr # Linear model for RFE

## Improt Statistics Libraries
import statsmodels.api as sm # Multiple regression model

## Import Predictor Datasets
os.chdir("C:/Users/drewc/GitHub/HNB/_data") # Set wd to project data repository
df_eco = pd.read.csv("acs_us_eco_stage.csv", encoding = "ISO-8859-1") # Selected Economic characertistics of the US Populaiton, American Communtiy Survey
df_hou = pd.read.csv("acs_us_house_stage.csv", encoding = "ISO-8859-1") # Selected Housing characertistics of the US Populaiton, American Communtiy Surve
df_soc = pd.read.csv("acs_us_social_stage.csv", encoding = "ISO-8859-1") # Selected Social characertistics of the US Populaiton, American Communtiy Surve
df_air = pd.read.csv("wonder_airqual_stage.csv", encoding = "ISO-8859-1") # Particulate matter in air, CDC Wonder
df_htw = pd.read.csv("wonder_heatwave_stage.csv", encoding = "ISO-8859-1") # Heat wave days per year, CDC Wonder
df_fod = pd.read.csv("usda_foodatlas_stage.csv", encoding = "ISO-8859-1") # Measures of food access, USDA food atlas
df_epa = pd.read.csv("epa_atlas_stage.csv", encoding = "ISO-8859-1") # Environmental compliance, EPA data atlas

## Import Outcome Datasets
df_out1 = pd.read.csv("health_out1_stage.csv", encoding = "ISO-8859-1") # Health outcome 1
df_out2 = pd.read.csv("health_out2_stage.csv", encoding = "ISO-8859-1") # Health outcome 2
df_out3 = pd.read.csv("health_out3_stage.csv", encoding = "ISO-8859-1") # Health outcome 3

## Join Predictor Datasets
df_m1 = pd.merge(df_eco, df_hou, on = "County", how = "inner") # Merge 1st and 2nd dataset
df_m2 = pd.merge(df_m2, df_soc, on = "County", how = "inner") # Merge 3rd with 1-2
df_m3 = pd.merge(df_m3, df_air, on = "County", how = "inner") # Merge 4th with 1-3
df_m4 = pd.merge(df_m4, df_htw, on = "County", how = "inner") # Merge 5th with 1-4
df_us = pd.merge(df_m5, df_fod, on = "County", how = "inner") # Merge 6th with 1-5 and name US

## Join Outcome Datasets
df_m1 = pd.merge(df_out1, df_out2, on = "County", how = "inner") # Merge 1st and 2nd dataset
df_out = pd.merge(df_m1, df_out3, on = "County", how = "inner") # Merge 3rd with 1-2

## Tidy Predictor Data
df_us = df_us.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_us = df_us.dropna() # Drop all rows with NA values

## Tidy Outcome Data
df_out = df_out.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric
df_out = df_out.dropna() # Drop all rows with NA values

## Verify
df_us.info() # Check variables and data types
df_us.head() # Check first 5 observations
df_out.info() # Check variables and data types
df_out.head() # Check first 5 observations

### Section 2: Use Random Forest to Classify Ecological Variables by Contribution to Outcome

## Setup Predictors and Forest
features = df_us.columns.drop(["County"]) # Drop GeoID variable to isolate all predictor variable names as features
X = df_us[features] # Save features columns as predictor data frame
Y = pd.factorize(df_out["Outcome"])[0] # Isolate Outcome variable and factorize as numbers
forest = rfc(n_estimators = 500, max_depth = 10) #Use default values except for number of trees. For a further explanation see readme included in repository. 

## Run Forest 
forest.fit(X, Y) # This will take time

## Output importances
gini = forest.feature_importances_ # Output importances of features
l_gini = list(zip(X, gini)) # Create list of variables alongside importance scores 
df_gini = pd.DataFrame(l_gini, columns = ["Variables", "Gini"]) # Create data frame of importances with variables and gini column names

## Select top 100 variables by gini coefficient
df_gini = df_gini.sort_values(by = ["Gini"], ascending = False) # Sort data frame by gini value in desceding order
df_gini = df_gini.reset_index(drop = True) # Reset index to match sorted data
df_gini = df_gini.iloc[:100] # Select top 100 variables by Gini coefficient

## Recombine with Outcome Data for repeated random forest
l_100 = df_gini["Variables"].tolist() # Save top 100 variables as list
df_100 = df_rf[l_100] # Subset original dataset with top 100 variable list
df_repeat = pd.concat([df_100, df_out], axis = 1) # Combine outcomes with top 100 variables 

## Verify
df_repeat.info()
df_repeat.head()

### Section 3: Repeat with Smaller Selection, but with more trees

## Setup Predictors and Forest
features = df_repeat.columns.drop(["Outcome"]) # Drop outcome variable and Geo to isolate all predictor variable names as features
X = df_repeat[features] # Save features columns as predictor data frame
Y = pd.factorize(df_repeat["Outcome"])[0] # Isolate Outcome variable and factorize as numbers
forest = rfc(n_estimators = 1000, max_depth = 10) #Use default values except for number of trees. For a further explanation see readme included in repository. 

## Run Forest
forest.fit(X, Y) # This will take time

## Output importances
gini = forest.feature_importances_ # Output importances of features
l_gini = list(zip(X, gini)) # Create list of variables alongside importance scores 
df_gini = pd.DataFrame(l_gini, columns = ["Variables", "Gini"]) # Create data frame of importances with variables and gini column names
df_gini.info() # Check importance data frame

## Select top 15 variables by gini coefficient
df_gini = df_gini.sort_values(by = ["Gini"], ascending = False) # Sort data frame by gini value in desceding order
df_gini = df_gini.reset_index(drop = True) # Reset index to match sorted data
df_gini = df_gini.iloc[:15] # Select top 15 variables by Gini coefficient

## Recombine with Outcome Data for RFE
l_15 = df_gini["Variables"].tolist() # Save top 15 variables as list
df_15 = df_rf[l_15] # Subset original dataset with top 15 variable list
df_rfe = pd.concat([df_15, df_out], axis = 1) # Combine outcomes with top 15 variables 

## Verify
df_rfe.info()
df_rfe.head()

### Section 4: Run Recursive Feature Selection to identify top 5 variables that contribute to outcome

## Setup Predictors and Forest
features = df_rfe.columns.drop(["Outcome"]) # Drop outcome variable and Geo to isolate all predictor variable names as features
X = df_rfe[features] # Save features columns as predictor data frame
Y = df_out # Use outcome data frame 
estimator = svr(kernel = "linear") # Use linear coefficient as estimator
selector = rfe(estimator, 5, step = 1) # define selection parameters, in this case 5 is selected. See Readme for more ifo

## Run Recursive Feature Selection
selected = selector.fit(X, Y) # This will take time

## Output RFE results
ar_bool = selected.support_ # Save Boolean values as numpy array
l_bool = list(zip(X, ar_bool)) # Create list of variables alongside RFE value 
df_bool = pd.DataFrame(l_bool, columns = ["Variables", "RFE"]) # Create data frame of importances with variables and gini column names
df_true = df_bool[df_bool.RFE == True]

## Recombine with Outcome Data for RFE
l_5 = df_true["Variables"].tolist() # Save 5 identified variables as list
df_model = df_rf[l_5] # Subset original dataset with identified variable list

## Verify
df_model.info()
df_model.head()

### Section 5: Create Linear Regression Model from 5 Variables to Predict Outcome

## Setup Predictors and Model
X = df_model # Use identified variables data frame from RFE
Y = df_out # Use original outcome variable for Y

## Run Linear Regression Model
model = sm.OLS(Y, X).fit() # This may but most likely wont take time

## Output Model
result = model.summary() # Create Summary of final model
print(result) # Print result to verify

## Write Summary to Text File
text_file = open("Neville/neville_outcome_results.txt", "a") # Open text file and name with subproject, content, and result suffix
text_file.write(str(result)) # write string version of summary result
text_file.close() # Close file

### Project Completed
print("THE END")







