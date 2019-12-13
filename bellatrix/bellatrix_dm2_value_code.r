#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Cedric subproject: Developing better ways to measure equity in health using the Gini coefficient
## Florida Charts Census Tract Mortality Data:  R Project for Statistical Computing Code Script by DrewC!

### Step 1: Import Libraries and Import Dataset

## Open R Terminal
R # open R in VS Code (any terminal)

## Import Standard Libraries
library(tidyverse)

## Import Machine Learning Libraries
library(randomForest) # Popular random forest package for R

## Import Statistics Libraries
library(MASS) # Stepwise inclusion model with linear and logistic options
library(psych) # Survey analysis library with factor analysis
library(GPArotation) # Rotation options for factor analysis
library(pROC) # ROC tests with AUC output
library(ineq) # Gini coefficient and Lorenz curve

## Import Data
setwd("C:/Users/drewc/GitHub/HNB") # Set wd to project repository
df_cedric = read.csv("_data/cedric_dm2_gini.csv") # Import dataset from _data folder
df_mungos = read.csv("_data/mungos_np_value.csv") # Import dataset from _data folder

## Tidy
df_cedric = df_cedric %>% mutate_if(is.factor, as.character) # Change character to numeric values
df_mungos = df_mungos %>% mutate_if(is.factor, as.character) # Change character to numeric values

## Join
df_bella = inner_join(df_cedric, df_mungos, by = "County")

## Verify
glimpse(df_bella)
glimpse(df_mungos)
glimpse(df_cedric)

### Step 2: Statistical Test

## Spearman's Rank for ERR
corr_err = cor.test(x = df_bella$Gini, y = df_bella$ERR, method = "spearman") # Pearson's Rank for Q->Q
print(corr_err)

## Spearman's Rank for MSPB
corr_gini = cor.test(x = df_bella$Gini, y = df_bella$MSPB, method = "spearman") # Pearson's Rank for Q->Q
print(corr_mspb)