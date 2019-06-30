## Code Prep

setwd("C:/Users/drewc/Documents/healthy_neighborhoods")

library(dplyr)
library(randomForest)
library(MASS)
library(reshape)

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

colnames(final) <- c("Estimate", "Std.Error", "t", "Pr.t")
finalcoef = final$Estimate
finalcoef = finalcoef[-1] 

finalvars = rownames(final)
finalvars = finalvars[-1] 
finalvars = c("With a Computer", "With Income from Earnings", "College Educated", "With a Disability", "85 Years and Over", "62 Years and Over", "Born in U.S.", "Not in Labor Force with Public Coverage", "Householder in Household", "Not in Labor Force", "Nonfamily Households", "English Only Households", "Households with Children", "Housing Value $50,000 to $99,999", "With Social Security", "Householder Living Alone", "Married Females", "Family Households", "Males Widowed", "65 and Over Households")                                      


barplot(finalcoef, names.arg = finalvars, main = "Social Variables Assocaited with Diabetets Mortality", xlab = "Coefficient in Final Fit Model", col = "blue", las = 1, horiz = TRUE)

write.csv(final, file = "C:/Users/drewc/Documents/healthy_neighborhoods/rf/rf_results_dmacs.csv")
