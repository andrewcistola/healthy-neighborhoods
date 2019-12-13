#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Cedric subproject: Developing better ways to measure equity in health
## Florida Charts Census Tract Mortality Data: Pyhton Computing Language Code Script by DrewC!

#### Section A: Import Libraries and Datasets and Prepare Data

### Import Libraries and Data

## Open R Terminal
R # open R in VS Code (any terminal)

## Import Hadley Wickham Libraries
library(tidyverse) # All of the libraries above in one line of code

## Import Statistics Libraries
library(ineq) # Gini coefficient and Lorenz curve
library(pROC) # ROC tests with AUC output

## Import Data
setwd("C:/Users/drewc/GitHub/HNB") # Set wd to project repository
df_fl = read.csv("_data/flcharts_50_stage.csv") # Import dataset from _data folder

### Step 2: Prepare Data for Classificaiton

## Tidy data types and objects
df_fl = na.omit(df_fl) # Omit rows with NA from Data Frame

## Verify Data
glimpse(df_fl) # Rows, columns, variable types and 10 

### Step 3: Develop Inequality Measures for Data

## Create new column as sum of others
df_fl$Vascular = df_fl$Heart.Diseases + df_fl$Cerebrovascular.Diseases +  df_fl$Essen.Hypertension...Hypertensive.Renal.Dis + df_fl$ Aortic.Aneurysm...Dissection + df_fl$Atherosclerosis  # Create new column based on conditions
df_fl$Metabolic = df_fl$Diabetes.Mellitus + df_fl$Nephritis..Nephrotic.Syndrome..Nephrosis # Create new column based on conditions
df_fl$MetaVasc = df_fl$Metabolic + df_fl$Vascular

## Group by County for internal Gini
tib_gini = df_fl %>% group_by(County) %>% summarise(ineq(Metabolic, type = "Gini")) # Group By Columns and Average
df_gini = as.data.frame(tib_gini) # Convert tiblle to Data Frame
colnames(df_gini) <- c("County", "Gini") # Change Column Names
df_gini$County = toupper(df_gini$County)

## Export County Gini Data
write.csv(df_gini, "_data/cedric_dm2_gini.csv") #clean in excel and select variable
