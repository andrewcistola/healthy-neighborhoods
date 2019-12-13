## Code Prep

setwd("C:/Users/drewc/Documents/GitHub")

library(dplyr)

## Join Datasets

acs <- read.csv("acs/acs_data_rates.csv")
flch <- read.csv("flcharts/flcharts_data_50rate.csv")

join = inner_join(acs, flch, by = "Tract")

write.csv(join, "C:/Users/drewc/Documents/healthy_neighborhoods/rf/rf_master_50acs.csv") #clean in excel and select variable
