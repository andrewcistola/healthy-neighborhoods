#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Neville Subproject: Using Random Forestes, Factor Analysis, and Recursive Feature Selection to Screen Variables for Imapcts on Public Health
## Florida Charts Diabetes Mortality by Census Tract: Pyhton Computing Language Code Script by DrewC!

### Section 1: Import Libraries, Import Dataset, Prepare for Classification

## Import Standard Libraries
import os # Inlcuded in every script DC!
import numpy as np # Inclduded in every code script DC!
import pandas as pd # Incldued in every code script for DC!

## Import Specific Libraries and Packages
import sklearn.ensemble # SciKit Learn package contains many classification options beyond those used below
from sklearn.ensemble import RandomForestClassifier as rfc # Random Forest classification component
from sklearn.feature_selection import RFE as rfe # Recursive Feature selection component
from sklearn.svm import SVR as svr # Linear model for RFE
import statsmodels.api as sm # Multiple regression model

## Import Dataset
os.chdir("C:/Users/drewc/GitHub/Healthy_Neighborhoods") # Set wd to project repository
df_nev = pd.read_csv("_data/neville_dm2_acs.csv", encoding = "ISO-8859-1", low_memory= False) # Import dataset with outcome and ecological variable for each geographical id, all datasets in _data folder in repository

## Verify
df_nev.info()

### Section 2: Use Random Forest to Classify Ecological Variables by Contribution to Outcome

## Tidy and Clean
df_rf = df_nev.drop(columns = ["County"]) # Drop Unwanted Columns
df_rf = df_rf.apply(pd.to_numeric, errors = "coerce") # Convert all columns to numeric

## Prepare for Classification
features = df_rf.columns.drop(["Tract", "Diabetes"]) # Drop outcome variable and Geo to isolate all predictor variable names as features
df_rf = df_rf.dropna() # Drop all rows with NA values
X = df_rf[features] # Save features columns as predictor data frame
Y = pd.factorize(df_rf["Diabetes"])[0] # Isolate Outcome variable and factorize as numbers
forest = rfc(n_estimators = 1000, max_depth = 10) #Use default values except for number of trees. For a further explanation see readme included in repository. 

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
df_out = df_nev.filter(["Diabetes", "Tract"])
df_repeat = pd.concat([df_100, df_out], axis = 1) # Combine outcomes with top 100 variables 

## Verify
df_repeat.info()
df_repeat.head()

### Section 3: Repeat with Smaller Selection, but with more trees

## Setup Predictors and Forest
df_repeat = df_repeat.dropna() # Drop all rows with NA values
features = df_repeat.columns.drop(["Diabetes", "Tract"]) # Drop outcome variable and Geo to isolate all predictor variable names as features
X = df_repeat[features] # Save features columns as predictor data frame
Y = pd.factorize(df_repeat["Diabetes"])[0] # Isolate Outcome variable and factorize as numbers
forest = rfc(n_estimators = 10000, max_depth = 10) #Use default values except for number of trees. For a further explanation see readme included in repository. 

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
df_rfe = df_rfe.dropna() # Drop all rows with NA values
features = df_rfe.columns.drop(["Diabetes", "Tract"]) # Drop outcome variable and Geo to isolate all predictor variable
features = df_rfe.columns.drop(["Diabetes"]) # Drop outcome variable and Geo to isolate all predictor variable names as features
X = df_rfe[features] # Save features columns as predictor data frame
Y = df_rfe["Diabetes"] # Use outcome data frame 
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
text_file = open("Neville/neville_diabetes_results.txt", "a") # Open text file and name with subproject, content, and result suffix
text_file.write(str(result)) # write string version of summary result
text_file.close() # Close file

### Project Completed
print("THE END")
