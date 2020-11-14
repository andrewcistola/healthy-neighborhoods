## Code Prep

setwd("C:/Users/drewc/Documents/...")

library(plyr)
library(dplyr)
library(randomForest)
library(MASS)

## Random Forest

rf = read.csv("rf/rf_data_ab.csv")

rf$Geo.Id <- NULL

rf = rf %>% mutate_if(is.factor, as.numeric)

of = randomForest(formula = Variable ~ ., data = rf, ntree = 1000, importance=TRUE)

rank = importance(of)

write.csv(rank, ".../rf/rf_results_rank.csv") # clean, select cutoff, transpose in excel 

## Bind Variables to Prep Model

rank = read.csv("rf/rf_results_cutoff.csv")

bind = rbind.fill(rank, rf)

write.csv(bind, ".../rf/rf_results_bind.csv") #remove NA and clean in excel

mod = read.csv("rf/rf_results_bind.csv")

frmla = as.formula(paste("Variable ~ ", paste(colnames(rank), collapse=" + "), sep = ""))

fit = lm(frmla, data=mod)

## Stepwise backwards Fit

back = stepAIC(fit, direction="backward")

final = data.frame(summary(back)$coefficients)

write.csv(final, file = ".../rf/rf_results_final.csv") #sort coefficients in excel
