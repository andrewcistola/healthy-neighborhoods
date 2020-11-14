# allocativ
# Healthy Neighborhoods
# ACS DP5Y2018 join Code
# FIPS sum, avg, gini code

## Import Libraries and Data

### Import Hadley Wickham Libraries
library(tidyverse) # All of the libraries above in one line of code

### Import Statistics Libraries
library(ineq) # Gini coefficient and Lorenz curve
library(pROC) # ROC tests with AUC output

### Import Data
setwd("C:/Users/drewc/GitHub/allocativ") # Set wd to project repository
df_ZCTA = read.csv("hnb/ACS/DP5Y2018/ACS_DP5Y2018_ZCTA_full.csv") # Import dataset from _data folder

### CLean Data
df_ZCTA = subset(df_ZCTA, select = -c(ZCTA, X, ST)) # Remove columns in dataframe
df_ZCTA[is.na(df_ZCTA)] <- 0 # Convert all NA to 0

### Convert all to numeric
df_FIPS = df_ZCTA
df_ZCTA = subset(df_ZCTA, select = -c(FIPS)) # Remove columns in dataframe
df_ZCTA = df_ZCTA %>% mutate_if(is.character, as.numeric) ## Change Characters to Numeric
df_ZCTA$FIPS = df_FIPS$FIPS

### Gini, Sum, AVG
tib_FIPS = df_ZCTA %>% group_by(FIPS) %>% summarise_all(.funs = list(gini = ~ ineq(x = ., type = "Gini"), avg = ~ mean(x = .))) # Group By Columns and Average
df_FIPS = as.data.frame(tib_FIPS) # Convert tiblle to Data Frame

### Export to CSV
write.csv(df_FIPS,"hnb/ACS/DP5Y2018/ACS_DP5Y2018_FIPS_gini.csv", row.names = FALSE)









