#### Hope Score Project: Using the YRBSS to predict youth suicide ideation
### Risk Score Development: Using Variable Classification SYstems to Build Regression Models and Risk Scores
## CDC Youth Behavioral Risk Surveillance Survey: Code Script by DrewC!

#### Section A: Prepare Code

### Step 1: Import Libraries and Import Dataset

## Open R Terminal
R # open R in VS Code (any terminal)

## Import Hadley Wickham Libraries
library(tidyverse) # All of the libraries above in one line of code
library(skimr) # Library used for easy summary of data

## Import Machine Learning Libraries
library(randomForest) # Popular random forest package for R

## Import Statistics Libraries
library(MASS) # Stepwise inclusion model with linear and logistic options
library(pROC) # ROC tests with AUC output
library(psych) # Survey analysis library with factor analysis
library(GPArotation) # Rotation options for factor analysis

## Import Data
setwd("C:/Users/drewc/GitHub/HNB") # Set wd to project repository
df_nhanes = read.csv("_data/nhanes_1516_noRX_stage.csv") # Import dataset from _data folder

## Verify
dim(df_nhanes)

### Step 2: Prepare Data for Classificaiton

## Subset for outcome of interest
df_nhanes$outcome <- 0 # Add new outcome column and set value to 0
df_nhanes$outcome[df_nhanes$LBXGH >= 5.7 & df_nhanes$LBXGH < 6.4] <- 1 # Create new column based on conditions
df_nhanes = subset(df_nhanes, select = -c(SEQN, LBXGH, DIQ010))

## Verify
head(df_nhanes$outcome)

## Resolve missing data
df_na = df_nhanes
df_na = df_na[-which(rowSums(is.na(df_na)) > 1089),] # Remove variables with high missing values
df_na = df_na[, -which(colSums(is.na(df_na)) > 3034)] # Remove variables with high missing values
df_na = df_na[-which(rowSums(is.na(df_na)) > 195),] # Remove variables with high missing values
df_na = df_na[, -which(colSums(is.na(df_na)) > 146)] # Remove variables with high missing values
df_na = subset(df_na, select = -c(AUATYMTL, SLQ300, SLQ310, AUATYMTR)) # Remove variables with factor value types
df_na = na.omit(df_na) # Omit rows with NA from Data Frame

## Name reduction data neville
df_nev = df_na

## Verify 
dim(df_na)
colnames(df_na)
median(rowSums(is.na(df_na)))
median(colSums(is.na(df_na)))

#### Section B: Vairable Selection using Quantitative and Qualitative Methods

### Step 3: Conduct Factor Analysis to Identify Latent Variables

## Subset by group with outcome
df_fa = subset(df_na, outcome == 1) # Subset for outcome of interest
df_fa = subset(df_fa, select = -(outcome)) # Remove outcome variable
df_fa = na.omit(df_fa)
nrow(df_fa) # Check number of rows

## Perform Scree test and loadings
cor_fa = cor(df_fa)
cor_fa[!is.finite(cor_fa)] <- 0
model_scree = fa.parallel(cor_fa) # Create scree plot to determine number of latent variables
print(model_scree)

## Write Scree Test Output to File
result = model_scree # Save result df to variable
file = file("neville/neville_nhanes_dm2_results.txt") # Open result file in subproject repository
open(file, "w") # Open file and "a" to append
write("Factor Analysis",  file) # Insert title
write(" ", file) # Insert space below title
write("Eigenvalues from Scree Test",  file) # Insert title
write(" ", file) # Insert space below title
capture.output(result, file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
close(file) # Close file

## Idenitfy Loadings
factors = fa(r = cor_fa, nfactors = 6)
df_load = as.data.frame(unclass(factors$loadings))
colMax <- function(data) sapply(data, max, na.rm = TRUE)

colMax(df_load)

## Identify Vairbles with Loadings over 0.5
df_ld = df_load
df_ld$factor1[df_ld$MR1 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor2[df_ld$MR2 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor3[df_ld$MR3 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor4[df_ld$MR4 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor5[df_ld$MR5 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor6[df_ld$MR6 > 0.5] <- 1 # Create new column based on conditions
df_ld = subset(df_ld, select = -c(MR1, MR2, MR3, MR4, MR5, MR6))

df_f1 = subset(df_ld, factor1 == 1) # Subset for outcome of interest
df_f1 = df_f1["factor1"]
df_f2 = subset(df_ld, factor2 == 1) # Subset for outcome of interest
df_f2 = df_f2["factor2"]
df_f3 = subset(df_ld, factor3 == 1) # Subset for outcome of 
df_f3 = df_f3["factor3"]
df_f4 = subset(df_ld, factor4 == 1) # Subset for outcome of interest
df_f4 = df_f4["factor4"]
df_f5 = subset(df_ld, factor5 == 1) # Subset for outcome of interest
df_f5 = df_f5["factor5"]
df_f6 = subset(df_ld, factor6 == 1) # Subset for outcome of interest
df_f6 = df_f6["factor6"]

## Write Scree Test Output to File
file = file("neville/neville_nhanes_dm2_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "a" to append
write("Factor Loadings",  file) # Insert title
write(" ", file) # Insert space below title
capture.output(df_f1, file = file, append = TRUE) # write summary to file
capture.output(df_f2, file = file, append = TRUE) # write summary to file
capture.output(df_f3, file = file, append = TRUE) # write summary to file
capture.output(df_f4, file = file, append = TRUE) # write summary to file
capture.output(df_f5, file = file, append = TRUE) # write summary to file
capture.output(df_f6, file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
close(file) # Close file

### Step 4: Use a Random Forest to rank variables by importance 

## Create a Random Forest
df_rf = df_nev
forest = randomForest(formula = outcome ~ ., data = df_rf, ntree = 1000, importance = TRUE) # This will take time
summary(forest) # Summary of forest model

## Tidy Results for Variable Classification
mat_forest = round(importance(forest), 2) # Round importance outcomes to two places,
df_forest = as.data.frame(mat_forest) # Save as data frame
df_forest = rownames_to_column(df_forest)
colnames(df_forest) <- c("Variable", "MSE", "Gini") # Change column names to easily readible. Both values correspond to the summed increse in either Mean Squared Error or Gini as the variable is removed. Both are important and used elsewhere in randomforests (Scikit-learn). 

## Create Importance Variable Lists
df_rank = arrange(df_forest, desc(Gini)) # Descend by variable in data frame
print(df_rank) # Print output

## Write Random Forest Output to File
result = print(df_rank) # Save result df to variable
file = file("neville/neville_nhanes_dm2_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "w" to overwrite
write("Random Forest Variable Classification", file) # Insert title
write(" ", file) # Insert space below title
write.table(result, file, quote = FALSE, sep = "   ") # write table of values to filee
write(" ", file) # Insert space below result
close(file) # Close file

### Summary Statistics of Model Variables
file = file("neville/neville_nhanes_pdm_fa_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "w" to overwrite
write("Summary of Model Variables", file) # Insert title
write(" ", file) # Insert space below result
write("BMXSAD1", file) # Insert space below title
capture.output(summary(df_nev$BMXSAD1), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("BPXSY1", file) # Insert space below title
capture.output(summary(df_nev$BPXSY1), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("LBXNEPCT", file) # Insert space below title
capture.output(summary(df_nev$LBXNEPCT), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("URDACT", file) # Insert space below title
capture.output(summary(df_nev$URDACT), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("HSQ510", file) # Insert space below title
capture.output(summary(df_nev$HSQ510), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("LBXSF3SI", file) # Insert space below title
capture.output(summary(df_nev$LBXSF3SI), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("CBD071", file) # Insert space below title
capture.output(summary(df_nev$CBD071), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("OHARNF", file) # Insert space below title
capture.output(summary(df_nev$OHARNF), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
close(file) # Close file

#### Section C: Build Regression Model and Risk Score for Validation 

### Step 5: Create Dichotomous Variables Based on 3rd Quartile

## Create New Variables
df_nh$SAD <- 0 # Add new outcome column and set value to 0
df_nh$SYS <- 0 # Add new outcome column and set value to 0
df_nh$NEU <- 0 # Add new outcome column and set value to 0
df_nh$ACR <- 0 # Add new outcome column and set value to 0
df_nh$STO <- 0 # Add new outcome column and set value to 0
df_nh$FOL <- 0 # Add new outcome column and set value to 0
df_nh$GRO <- 0 # Add new outcome column and set value to 0
df_nh$ORL <- 0 # Add new outcome column and set value to 0
df_nh$SAD[df_nh$BMXSAD1 > 25.6] <- 1 # Create new column based on conditions
df_nh$SYS[df_nh$BPXSY1 > 130] <- 1 # Create new column based on conditions
df_nh$NEU[df_nh$LBXNEPCT > 50.95] <- 1 # Create new column based on conditions
df_nh$ACR[df_nh$URDACT > 4.64] <- 1 # Create new column based on conditions
df_nh$STO[df_nh$HSQ510 == 1] <- 1 # Create new column based on conditions
df_nh$FOL[df_nh$LBXSF3SI > 0.1410] <- 1 # Create new column based on conditions
df_nh$GRO[df_nh$CBD071 > 526] <- 1 # Create new column based on conditions
df_nh$ORL[df_nh$OHARNF != 0] <- 1 # Create new column based on conditions

## Resolve missing data
df_lon = subset(df_nh, select = c(outcome, SAD, SYS, NEU, ACR, STO, FOL, GRO, ORL)) # Remove variables with factor value types
df_lon = na.omit(df_lon) # Omit rows with NA from Data Frame
dim(df_lon)

### Step 6: Logistic Regression with Stepwise Selection for Final Model

## Create training and validation set
sample = sample.int(n = nrow(df_lon), size = floor(.50*nrow(df_lon)), replace = F) # Create training and testing dataset with 50% split
train = df_lon[sample, ] # Susbset data frame by sample
test = df_lon[-sample, ] # Subset data frame by removing sample

## Perform Logisitc Regression on selected variables
model_logistic = glm(outcome ~ SAD + SYS + NEU + ACR + STO + FOL + GRO + ORL, data = train)
summary(model_logistic)

## Stepwise backward selection
model_back = stepAIC(model_logistic, direction = "backward") # Stepwise backwards selection on model
summary(model_back) # Output model summary and check for variables to remove for final model

## Write Quantitative Selection Model Output to File
result1 = print(summary(model_logistic)) # Save result df to variable
result2 = print(summary(model_back)) # Save result df to variable
file = file("neville/neville_nhanes_pdm_fa_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "a" to append
write("Logistic Regression Model", file) # Insert space below title
write(" ", file) # Insert space below title
capture.output(result, file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below title
write("Stepwise Backwards Selection", file) # Insert space below title
write(" ", file) # Insert space below title
capture.output(result2, file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below title
close(file) # Close file

### Step 7: Create Score and Verify

# Create new column based on conditions
test$score <- 0 # Add new outcome column and set value to 0
test$score = (11*test$SAD) + (13*test$SYS) + (6*test$NEU) + (2*test$ACR) + (2*test$GRO) + (2*test$ORL) 
df_nh$score <- 0
df_nh$score = (11*df_nh$SAD) + (13*df_nh$SYS) + (6*df_nh$NEU) + (2*df_nh$ACR) + (2*df_nh$GRO) + (2*df_nh$ORL) 

## Final Model and AUC Score
model_score = glm(outcome~ score, data = test) # Perform logistic regression model on selected variables on test data
roc_test = roc(model_score$y, model_score$fitted.values, ci = T, plot = T) # Perform ROC test on test data
auc(roc_test) # Print AUC score

## Write Quantitative Selection Model Output to File
result = print(auc(roc_test)) # Save result df to variable
file = file("neville/neville_nhanes_pdm_fa_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "a" to append
write("Risk Score Validation", file) # Insert space below title
write(" ", file) # Insert space below title
capture.output(result, file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below title
close(file) # Close file

### Step 9: Create Score with Simple Values and Non-Lab Tests

## Create New Variables
df_nh$SAD <- 0 # Add new outcome column and set value to 0
df_nh$SYS <- 0 # Add new outcome column and set value to 0
df_nh$STO <- 0 # Add new outcome column and set value to 0
df_nh$GRO <- 0 # Add new outcome column and set value to 0
df_nh$ORL <- 0 # Add new outcome column and set value to 0
df_nh$SAD[df_nh$BMXSAD1 > 25.6] <- 1 # Create new column based on conditions
df_nh$SYS[df_nh$BPXSY1 > 130] <- 1 # Create new column based on conditions
df_nh$STO[df_nh$HSQ510 != 1] <- 1 # Create new column based on conditions
df_nh$GRO[df_nh$CBD071 < 500] <- 1 # Create new column based on conditions
df_nh$ORL[df_nh$OHARNF != 1] <- 1 # Create new column based on conditions

## Resolve missing data
df_lon = subset(df_nh, select = c(outcome, SAD, SYS, STO, GRO, ORL)) # Remove variables with factor value types
df_lon = na.omit(df_lon) # Omit rows with NA from Data Frame
dim(df_lon)

## Create training and validation set
sample = sample.int(n = nrow(df_lon), size = floor(.50*nrow(df_lon)), replace = F) # Create training and testing dataset with 50% split
train = df_lon[sample, ] # Susbset data frame by sample
test = df_lon[-sample, ] # Subset data frame by removing sample

## Perform Logisitc Regression on selected variables
model_logistic2 = glm(outcome ~ SAD + SYS + STO + GRO + ORL, data = train)
summary(model_logistic2)

# Create new column based on conditions
test$score <- 0 # Add new outcome column and set value to 0
test$score = (13*test$SAD) + (14*test$SYS) + (5*test$STO) + (3*test$GRO) + (2*test$ORL) 
df_nh$score <- 0
df_nh$score = (13*df_nh$SAD) + (14*df_nh$SYS) + (5*df_nh$STO) + (3*df_nh$GRO) + (29*df_nh$ORL)

## Resolve missing data
df_lon = subset(df_nh, select = c(outcome, SAD, SYS, STO, GRO, ORL)) # Remove variables with factor value types
df_lon = na.omit(df_lon) # Omit rows with NA from Data Frame
dim(df_lon)

## Final Model and AUC Score
model_score = glm(outcome~ score, data = test) # Perform logistic regression model on selected variables on test data
roc_test = roc(model_score$y, model_score$fitted.values, ci = T, plot = T) # Perform ROC test on test data
auc(roc_test) # Print AUC score
