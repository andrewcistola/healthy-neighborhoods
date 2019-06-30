## Code Prep

setwd("C:/Users/drewc/Documents/...")

library(dplyr)

## Join Datasets

a <- read.csv("data1/data1_data_a.csv")
b <- read.csv("data2/data2_data_b.csv")

join = inner_join(a, b, by = "Geo.Id")

write.csv(join, ".../rf/rf_data_ab.csv") #clean in excel
