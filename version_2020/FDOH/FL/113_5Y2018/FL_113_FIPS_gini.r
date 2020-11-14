# allocativ
# Healthy Neighborhoods
# ACS DP5Y2018 join Code
# FIPS sum, avg, gini code

### Import Hadley Wickham Libraries
library(tidyverse) # All of the libraries above in one line of code

### Import Statistics Libraries
library(ineq) # Gini coefficient and Lorenz curve
library(pROC) # ROC tests with AUC output

### Set wd
setwd("C:/Users/drewc/GitHub/allocativ") # Set wd to project repository

### Import data
df_doh = read.csv("hnb/DOH/FL/113_5Y2018/FL_113_ZCTA.csv") # Import dataset from _data folder
df_key = read.csv("hnb/FIPS/FIPS_ZCTA_key.csv") # Import dataset from _data folder

### Join with key
df_key = subset(df_key, select = c(FIPS, ZCTA)) # Remove variables with high missing values
df_join = inner_join(df_key, df_doh, by = "ZCTA") ## Join By Columns

### Clean Data
df_join[is.na(df_join)] <- 0 # Convert all NA to 0

### Convert all to numeric
df_num = subset(df_join, select = -c(FIPS, ZCTA, PERCENT_TOTAL, POPULATION)) # Remove columns in dataframe
df_num = df_num %>% mutate_if(is.character, as.numeric) ## Change Characters to Numeric
df_num$FIPS = df_join$FIPS

### Gini, Avg
tib_FIPS = df_num %>% group_by(FIPS) %>% summarise_all(.funs = list(gini = ~ ineq(x = ., type = "Gini"), avg = ~ mean(x = .))) # Group By Columns and Average
df_FIPS = as.data.frame(tib_FIPS) # Convert tiblle to Data Frame

### Export to CSV
write.csv(df_FIPS, "hnb/DOH/FL/113_5Y2018/FL_113_FIPS_gini.csv", row.names = FALSE)









