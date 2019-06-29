## Code Prep

setwd("C:/Users/drewc/Documents/healthy_neighborhoods")

library(dplyr)
library(randomForest)
library(MASS)
library(reshape)

## Join Datasets

acs <- read.csv("acs/acs_data_rates.csv")
flch <- read.csv("flcharts/flcharts_data_50rate.csv")

join = inner_join(acs, flch, by = "Tract")

write.csv(join, "C:/Users/drewc/Documents/healthy_neighborhoods/rf/rf_master_50acs.csv") #clean in excel and select variable

## Random Forest

rf = read.csv("rf/rf_master_dmacs.csv")

rf$Tract <- NULL

rf = rf %>% mutate_if(is.factor, as.numeric)

of <- randomForest(
  formula = Diabetes ~ ., 
  data = rf, 
  ntree = 1000,
  importance=TRUE)

rank = importance(of)

write.csv(rank, "C:/Users/drewc/Documents/healthy_neighborhoods/rf/rf_results_rank.csv") # clean and transpose in excel

## Bind Variables to Prep Model

rank = read.csv("rf/rf_results_rank41.csv")
rf = read.csv("rf/rf_master_dmacs.csv")

bind = rbind.fill(rank, rf)

write.csv(bind, "C:/Users/drewc/Documents/healthy_neighborhoods/rf/rf_results_bind.csv") #remove NA and clean in excel
mod = read.csv("rf/rf_results_bind.csv")

frmla = as.formula(paste("Diabetes ~ ", paste(colnames(rank), collapse=" + "), sep = ""))

fit = lm(frmla, data=mod)

## Stepwise backwards Fit

back <- stepAIC(fit, direction="backward")

final <- data.frame(summary(back)$coefficients)

write.csv(final, file = "C:/Users/drewc/Documents/healthy_neighborhoods/rf/rf_results_final.csv") #sort coefficients in excel
