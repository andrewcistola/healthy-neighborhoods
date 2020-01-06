<<<<<<< HEAD
#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Neville Subproject: Using Random Forestes, Factor Analysis, and Logistic regression to Screen Variables for Imapcts on Public Health
## National Health and Nutrition Examination Survey: The R Project for Statistical Computing Script by DrewC!
# Detecting Prediabetes in those under 65

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
setwd("C:/Users/drewc/GitHub/Healthy_Neighborhoods") # Set wd to project repository
df_nhanes = read.csv("_data/nhanes_1516_noRX_stage.csv") # Import dataset from _data folder

## Verify
dim(df_nhanes)

### Step 2: Prepare Data for Classificaiton

## Subset for outcome of interest
df_nhanes$outcome <- 0 # Add new outcome column and set value to 0
df_nhanes$outcome[df_nhanes$LBXGH >= 5.7 & df_nhanes$LBXGH < 6.4 ] <- 1 # Create new column based on conditions
df_nh = subset(df_nhanes, select = -c(SEQN, LBXGH, DIQ010))

## Resolve missing data
df_nev = df_nh[, -which(colSums(is.na(df_nh)) > 3646)] # Remove variables with high missing values
df_nev = subset(df_nev, select = -c(AUATYMTL, SLQ300, SLQ310, AUATYMTR)) # Remove variables with factor value types
df_nev = na.omit(df_nev) # Omit rows with NA from Data Frame
df_nev = df_nev[which(df_nev$RIDAGEYR < 65), ]

## Verify 
dim(df_nev)
colnames(df_nev)

#### Section B: Vairable Selection using Quantitative and Qualitative Methods

### Step 3: Conduct Factor Analysis to Identify Latent Variables

## Subset by group with outcome
df_fa = subset(df_nev, outcome == 1) # Subset for outcome of interest
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
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "w") # Open file and "a" to append
write("Factor Analysis",  file) # Insert title
write(" ", file) # Insert space below title
write("Eigenvalues from Scree Test",  file) # Insert title
write(" ", file) # Insert space below title
capture.output(result, file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
close(file) # Close file

## Idenitfy Loadings
factors = fa(r = cor_fa, nfactors = 10)
df_load = as.data.frame(unclass(factors$loadings))
df_ld = df_load[, which(apply(df_load, 2, max) > 0.5)] # Remove variables with high missing values
colnames(df_ld)

df_ld$factor1[df_ld$MR1 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor2[df_ld$MR2 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor3[df_ld$MR3 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor4[df_ld$MR4 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor5[df_ld$MR5 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor6[df_ld$MR6 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor7[df_ld$MR7 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor8[df_ld$MR8 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor9[df_ld$MR9 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor10[df_ld$MR10 > 0.5] <- 1 # Create new column based on conditions
df_ld = subset(df_ld, select = -c(MR1, MR2, MR3, MR4, MR5, MR6, MR7, MR8, MR9, MR10))

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
df_f7 = subset(df_ld, factor7 == 1) # Subset for outcome of interest
df_f7 = df_f7["factor7"]
df_f8 = subset(df_ld, factor8 == 1) # Subset for outcome of interest
df_f8 = df_f8["factor8"]
df_f9 = subset(df_ld, factor9 == 1) # Subset for outcome of interest
df_f9 = df_f9["factor9"]
df_f10 = subset(df_ld, factor10 == 1) # Subset for outcome of interest
df_f10 = df_f10["factor10"]

## Write Scree Test Output to File
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "a" to append
write("Factor Loadings",  file) # Insert title
write(" ", file) # Insert space below title
capture.output(df_f1, file = file, append = TRUE) # write summary to file
capture.output(df_f2, file = file, append = TRUE) # write summary to file
capture.output(df_f3, file = file, append = TRUE) # write summary to file
capture.output(df_f4, file = file, append = TRUE) # write summary to file
capture.output(df_f5, file = file, append = TRUE) # write summary to file
capture.output(df_f6, file = file, append = TRUE) # write summary to file
capture.output(df_f7, file = file, append = TRUE) # write summary to file
capture.output(df_f8, file = file, append = TRUE) # write summary to file
capture.output(df_f9, file = file, append = TRUE) # write summary to file
capture.output(df_f10, file = file, append = TRUE) # write summary to file
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
df_rank = df_rank[which(df_rank$Gini > 0 & df_rank$MSE > 0), ]
print(df_rank) # Print output

## Write Random Forest Output to File
result = print(df_rank) # Save result df to variable
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "w" to overwrite
write("Random Forest Variable Classification", file) # Insert title
write(" ", file) # Insert space below title
write.table(result, file, quote = FALSE, sep = "   ") # write table of values to filee
write(" ", file) # Insert space below result
close(file) # Close file

### Summary Statistics of Model Variables
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "w" to overwrite
write("Summary of Model Variables", file) # Insert title
write(" ", file) # Insert space below result
write("OHX19TC", file) # Insert space below title
capture.output(summary(df_nev$OHX19TC), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("BMDAVSAD", file) # Insert space below title
capture.output(summary(df_nev$BMDAVSAD), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("INDFMMPI", file) # Insert space below title
capture.output(summary(df_nev$INDFMMPI), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("INQ080", file) # Insert space below title
capture.output(summary(df_nev$INQ080), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("BMXLEG", file) # Insert space below title
capture.output(summary(df_nev$BMXLEG), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("LBXWBCSI", file) # Insert space below title
capture.output(summary(df_nev$LBXWBCSI), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("LBXRDW", file) # Insert space below title
capture.output(summary(df_nev$LBXRDW), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("BPXDI3", file) # Insert space below title
capture.output(summary(df_nev$BPXDI3), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("LBDRFO", file) # Insert space below title
capture.output(summary(df_nev$LBDRFO), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
close(file) # Close file

### Step 5: Liner Regression to Determine Direction of Impact

model_logistic <- glm(outcome~ OHX19TC + BMDAVSAD + INDFMMPI + INQ080 + BMXLEG + LBXWBCSI + LBXRDW + BPXDI3 + LBDRFO, data = df_nev)
summary(model_logistic)

## Write Model Output to File
result = summary(model_logistic) # Save result df to variable
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "a" to append
write(" ", file) # Insert space below title
write("First Logistic Regression for Variable Direction",  file) # Insert title
write(" ", file) # Insert space below title
capture.output(result, file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
close(file) # Close file

#### Section C: Build Regression Model and Risk Score for Validation 

### Step 5: Create Dichotomous Variables Based on 3rd Quartile

## Create New Variables
df_nh$V1 <- 0 # Add new outcome column and set value to 0
df_nh$V2 <- 0 # Add new outcome column and set value to 0
df_nh$V3 <- 0 # Add new outcome column and set value to 0
df_nh$V4 <- 0 # Add new outcome column and set value to 0
df_nh$V5 <- 0 # Add new outcome column and set value to 0
df_nh$V1[df_nh$OHX01TC == 4 | df_nh$OHX02TC == 4 | df_nh$OHX03TC == 4 | df_nh$OHX04TC == 4 | df_nh$OHX05TC == 4 | df_nh$OHX06TC == 4 | df_nh$OHX07TC == 4 | df_nh$OHX08TC == 4 | df_nh$OHX09TC == 4 | df_nh$OHX10TC == 4 | df_nh$OHX11TC == 4 | df_nh$OHX12TC == 4 | df_nh$OHX13TC == 4 | df_nh$OHX14TC == 4 | df_nh$OHX15TC == 4 | df_nh$OHX16TC == 4 | df_nh$OHX17TC == 4 | df_nh$OHX18TC == 4 | df_nh$OHX19TC == 4 | df_nh$OHX20TC == 4 | df_nh$OHX21TC == 4 | df_nh$OHX22TC == 4 | df_nh$OHX23TC == 4 | df_nh$OHX24TC == 4 | df_nh$OHX25TC == 4 | df_nh$OHX26TC == 4 | df_nh$OHX27TC == 4 | df_nh$OHX28TC == 4 | df_nh$OHX29TC == 4 | df_nh$OHX30TC == 4 | df_nh$OHX31TC == 4 | df_nh$OHX32TC == 4] <- 1 # Create new column based on conditions
df_nh$V2[df_nh$BMDAVSAD > 25.1] <- 1 # Create new column based on conditions
df_nh$V3[df_nh$INDFMMPI > 5] <- 1 # Create new column based on conditions
df_nh$V4[df_nh$INQ080 == 1] <- 1 # Create new column based on conditions
df_nh$V5[df_nh$BMXLEG < 41.58] <- 1 # Create new column based on conditions

## Resolve missing data
df_lon = subset(df_nh, select = c(outcome, V1, V2, V3, V4, V5)) # Remove variables with factor value types
df_lon = na.omit(df_lon) # Omit rows with NA from Data Frame
dim(df_lon)

### Step 6: Logistic Regression with Stepwise Selection for Final Model

## Create training and validation set
sample = sample.int(n = nrow(df_lon), size = floor(.50*nrow(df_lon)), replace = F) # Create training and testing dataset with 50% split
train = df_lon[sample, ] # Susbset data frame by sample
test = df_lon[-sample, ] # Subset data frame by removing sample

## Perform Logisitc Regression on selected variables
model_logistic = glm(outcome~ V1 + V2 + V3 + V4 + V5, data = train)
summary(model_logistic)

## Stepwise backward selection
model_back = stepAIC(model_logistic, direction = "backward") # Stepwise backwards selection on model
summary(model_back) # Output model summary and check for variables to remove for final model

## Write Quantitative Selection Model Output to File
result1 = print(summary(model_logistic)) # Save result df to variable
result2 = print(summary(model_back)) # Save result df to variable
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "a" to append
write("Training Logistic Regression Model", file) # Insert space below title
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
test$score = (20*test$V2) + (15*test$V4) + (10*test$V5)

## Final Model and AUC Score
model_score = glm(outcome~ score, data = test) # Perform logistic regression model on selected variables on test data
roc_test = roc(model_score$y, model_score$fitted.values, ci = T, plot = T) # Perform ROC test on test data
auc(roc_test) # Print AUC score

## Write Quantitative Selection Model Output to File
result = print(auc(roc_test)) # Save result df to variable
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "a" to append
write("Risk Score Validation", file) # Insert space below title
write(" ", file) # Insert space below title
capture.output(result, file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below title
close(file) # Close file

=======
#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Neville Subproject: Using Random Forestes, Factor Analysis, and Logistic regression to Screen Variables for Imapcts on Public Health
## National Health and Nutrition Examination Survey: The R Project for Statistical Computing Script by DrewC!
# Detecting Prediabetes in those under 65

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
setwd("C:/Users/drewc/GitHub/Healthy_Neighborhoods") # Set wd to project repository
df_nhanes = read.csv("_data/nhanes_1516_noRX_stage.csv") # Import dataset from _data folder

## Verify
dim(df_nhanes)

### Step 2: Prepare Data for Classificaiton

## Subset for outcome of interest
df_nhanes$outcome <- 0 # Add new outcome column and set value to 0
df_nhanes$outcome[df_nhanes$LBXGH >= 5.7 & df_nhanes$LBXGH < 6.4 ] <- 1 # Create new column based on conditions
df_nh = subset(df_nhanes, select = -c(SEQN, LBXGH, DIQ010))

## Resolve missing data
df_nev = df_nh[, -which(colSums(is.na(df_nh)) > 3646)] # Remove variables with high missing values
df_nev = subset(df_nev, select = -c(AUATYMTL, SLQ300, SLQ310, AUATYMTR)) # Remove variables with factor value types
df_nev = na.omit(df_nev) # Omit rows with NA from Data Frame
df_nev = df_nev[which(df_nev$RIDAGEYR < 65), ]

## Verify 
dim(df_nev)
colnames(df_nev)

#### Section B: Vairable Selection using Quantitative and Qualitative Methods

### Step 3: Conduct Factor Analysis to Identify Latent Variables

## Subset by group with outcome
df_fa = subset(df_nev, outcome == 1) # Subset for outcome of interest
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
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "w") # Open file and "a" to append
write("Factor Analysis",  file) # Insert title
write(" ", file) # Insert space below title
write("Eigenvalues from Scree Test",  file) # Insert title
write(" ", file) # Insert space below title
capture.output(result, file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
close(file) # Close file

## Idenitfy Loadings
factors = fa(r = cor_fa, nfactors = 10)
df_load = as.data.frame(unclass(factors$loadings))
df_ld = df_load[, which(apply(df_load, 2, max) > 0.5)] # Remove variables with high missing values
colnames(df_ld)

df_ld$factor1[df_ld$MR1 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor2[df_ld$MR2 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor3[df_ld$MR3 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor4[df_ld$MR4 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor5[df_ld$MR5 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor6[df_ld$MR6 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor7[df_ld$MR7 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor8[df_ld$MR8 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor9[df_ld$MR9 > 0.5] <- 1 # Create new column based on conditions
df_ld$factor10[df_ld$MR10 > 0.5] <- 1 # Create new column based on conditions
df_ld = subset(df_ld, select = -c(MR1, MR2, MR3, MR4, MR5, MR6, MR7, MR8, MR9, MR10))

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
df_f7 = subset(df_ld, factor7 == 1) # Subset for outcome of interest
df_f7 = df_f7["factor7"]
df_f8 = subset(df_ld, factor8 == 1) # Subset for outcome of interest
df_f8 = df_f8["factor8"]
df_f9 = subset(df_ld, factor9 == 1) # Subset for outcome of interest
df_f9 = df_f9["factor9"]
df_f10 = subset(df_ld, factor10 == 1) # Subset for outcome of interest
df_f10 = df_f10["factor10"]

## Write Scree Test Output to File
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "a" to append
write("Factor Loadings",  file) # Insert title
write(" ", file) # Insert space below title
capture.output(df_f1, file = file, append = TRUE) # write summary to file
capture.output(df_f2, file = file, append = TRUE) # write summary to file
capture.output(df_f3, file = file, append = TRUE) # write summary to file
capture.output(df_f4, file = file, append = TRUE) # write summary to file
capture.output(df_f5, file = file, append = TRUE) # write summary to file
capture.output(df_f6, file = file, append = TRUE) # write summary to file
capture.output(df_f7, file = file, append = TRUE) # write summary to file
capture.output(df_f8, file = file, append = TRUE) # write summary to file
capture.output(df_f9, file = file, append = TRUE) # write summary to file
capture.output(df_f10, file = file, append = TRUE) # write summary to file
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
df_rank = df_rank[which(df_rank$Gini > 0 & df_rank$MSE > 0), ]
print(df_rank) # Print output

## Write Random Forest Output to File
result = print(df_rank) # Save result df to variable
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "w" to overwrite
write("Random Forest Variable Classification", file) # Insert title
write(" ", file) # Insert space below title
write.table(result, file, quote = FALSE, sep = "   ") # write table of values to filee
write(" ", file) # Insert space below result
close(file) # Close file

### Summary Statistics of Model Variables
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "w" to overwrite
write("Summary of Model Variables", file) # Insert title
write(" ", file) # Insert space below result
write("OHX19TC", file) # Insert space below title
capture.output(summary(df_nev$OHX19TC), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("BMDAVSAD", file) # Insert space below title
capture.output(summary(df_nev$BMDAVSAD), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("INDFMMPI", file) # Insert space below title
capture.output(summary(df_nev$INDFMMPI), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("INQ080", file) # Insert space below title
capture.output(summary(df_nev$INQ080), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("BMXLEG", file) # Insert space below title
capture.output(summary(df_nev$BMXLEG), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("LBXWBCSI", file) # Insert space below title
capture.output(summary(df_nev$LBXWBCSI), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("LBXRDW", file) # Insert space below title
capture.output(summary(df_nev$LBXRDW), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("BPXDI3", file) # Insert space below title
capture.output(summary(df_nev$BPXDI3), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
write("LBDRFO", file) # Insert space below title
capture.output(summary(df_nev$LBDRFO), file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
close(file) # Close file

### Step 5: Liner Regression to Determine Direction of Impact

model_logistic <- glm(outcome~ OHX19TC + BMDAVSAD + INDFMMPI + INQ080 + BMXLEG + LBXWBCSI + LBXRDW + BPXDI3 + LBDRFO, data = df_nev)
summary(model_logistic)

## Write Model Output to File
result = summary(model_logistic) # Save result df to variable
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "a" to append
write(" ", file) # Insert space below title
write("First Logistic Regression for Variable Direction",  file) # Insert title
write(" ", file) # Insert space below title
capture.output(result, file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below result
close(file) # Close file

#### Section C: Build Regression Model and Risk Score for Validation 

### Step 5: Create Dichotomous Variables Based on 3rd Quartile

## Create New Variables
df_nh$V1 <- 0 # Add new outcome column and set value to 0
df_nh$V2 <- 0 # Add new outcome column and set value to 0
df_nh$V3 <- 0 # Add new outcome column and set value to 0
df_nh$V4 <- 0 # Add new outcome column and set value to 0
df_nh$V5 <- 0 # Add new outcome column and set value to 0
df_nh$V1[df_nh$OHX01TC == 4 | df_nh$OHX02TC == 4 | df_nh$OHX03TC == 4 | df_nh$OHX04TC == 4 | df_nh$OHX05TC == 4 | df_nh$OHX06TC == 4 | df_nh$OHX07TC == 4 | df_nh$OHX08TC == 4 | df_nh$OHX09TC == 4 | df_nh$OHX10TC == 4 | df_nh$OHX11TC == 4 | df_nh$OHX12TC == 4 | df_nh$OHX13TC == 4 | df_nh$OHX14TC == 4 | df_nh$OHX15TC == 4 | df_nh$OHX16TC == 4 | df_nh$OHX17TC == 4 | df_nh$OHX18TC == 4 | df_nh$OHX19TC == 4 | df_nh$OHX20TC == 4 | df_nh$OHX21TC == 4 | df_nh$OHX22TC == 4 | df_nh$OHX23TC == 4 | df_nh$OHX24TC == 4 | df_nh$OHX25TC == 4 | df_nh$OHX26TC == 4 | df_nh$OHX27TC == 4 | df_nh$OHX28TC == 4 | df_nh$OHX29TC == 4 | df_nh$OHX30TC == 4 | df_nh$OHX31TC == 4 | df_nh$OHX32TC == 4] <- 1 # Create new column based on conditions
df_nh$V2[df_nh$BMDAVSAD > 25.1] <- 1 # Create new column based on conditions
df_nh$V3[df_nh$INDFMMPI > 5] <- 1 # Create new column based on conditions
df_nh$V4[df_nh$INQ080 == 1] <- 1 # Create new column based on conditions
df_nh$V5[df_nh$BMXLEG < 41.58] <- 1 # Create new column based on conditions

## Resolve missing data
df_lon = subset(df_nh, select = c(outcome, V1, V2, V3, V4, V5)) # Remove variables with factor value types
df_lon = na.omit(df_lon) # Omit rows with NA from Data Frame
dim(df_lon)

### Step 6: Logistic Regression with Stepwise Selection for Final Model

## Create training and validation set
sample = sample.int(n = nrow(df_lon), size = floor(.50*nrow(df_lon)), replace = F) # Create training and testing dataset with 50% split
train = df_lon[sample, ] # Susbset data frame by sample
test = df_lon[-sample, ] # Subset data frame by removing sample

## Perform Logisitc Regression on selected variables
model_logistic = glm(outcome~ V1 + V2 + V3 + V4 + V5, data = train)
summary(model_logistic)

## Stepwise backward selection
model_back = stepAIC(model_logistic, direction = "backward") # Stepwise backwards selection on model
summary(model_back) # Output model summary and check for variables to remove for final model

## Write Quantitative Selection Model Output to File
result1 = print(summary(model_logistic)) # Save result df to variable
result2 = print(summary(model_back)) # Save result df to variable
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "a" to append
write("Training Logistic Regression Model", file) # Insert space below title
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
test$score = (20*test$V2) + (15*test$V4) + (10*test$V5)

## Final Model and AUC Score
model_score = glm(outcome~ score, data = test) # Perform logistic regression model on selected variables on test data
roc_test = roc(model_score$y, model_score$fitted.values, ci = T, plot = T) # Perform ROC test on test data
auc(roc_test) # Print AUC score

## Write Quantitative Selection Model Output to File
result = print(auc(roc_test)) # Save result df to variable
file = file("neville/neville_nhanes_pdm_under_results.txt") # Open result file in subproject repository
open(file, "a") # Open file and "a" to append
write("Risk Score Validation", file) # Insert space below title
write(" ", file) # Insert space below title
capture.output(result, file = file, append = TRUE) # write summary to file
write(" ", file) # Insert space below title
close(file) # Close file

>>>>>>> 321eaea894d29a3f212ee3e111b86695f46cf6db
