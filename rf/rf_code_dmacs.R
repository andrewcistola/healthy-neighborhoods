## Join Datasets

library(dplyr)

setwd("C:/Users/drewc/Documents/healthy_neighborhoods")

acs <- read.csv("acs/acs_data_rates.csv")
flch <- read.csv("flcharts/flcharts_data_50rate.csv")

join = inner_join(acs, flch, by = "Tract")

write.csv(join, "C:/Users/drewc/Documents/healthy_neighborhoods/rf/rf_master_50acs.csv")

## Random Forest

library(randomForest)

rf = read.csv("rf/rf_master_dmacs.csv")

rf$Tract <- NULL

rf = rf %>% mutate_if(is.factor, as.numeric)

str(rf)

of <- randomForest(
  formula = Diabetes ~ ., 
  data = rf, 
  ntree = 1000,
  importance=TRUE)
  
## 

of = round(importance(output.forest), 2)

of = as.data.frame(of)

of = rownames_to_column(of)

of = select(of, rowname, "%IncMSE")

of = rename(of, Variable = rowname)

of <- of[order(-VarImp2$`%IncMSE`),]

## Stepwise backwards multuple regression model

library(MASS)

SortData = Step3 %>% top_n(20)

SortData1 <- SortData$Variable

SortData2 <- Step2[SortData1]

SortData2$Diabetes <- Step2$diabetes_crude_prev

SortData3 = paste(SortData$Variable, collapse = " + ")

print(SortData3)

fit <- lm(Diabetes~ percent_health_insurance_coverage_civilian_noninstitutionalized_population_with_health_insurance_coverage_with_public_coverage + percent_health_insurance_coverage_civilian_noninstitutionalized_population_with_health_insurance_coverage_with_private_health_insurance + percent_income_and_benefits_in_2016_inflation_adjusted_dollars_with_earnings + percent_income_and_benefits_in_2016_inflation_adjusted_dollars_with_food_stamp_snap_benefits_in_the_past_12_months + percent_educational_attainment_percent_high_school_graduate_or_higher + percent_employment_status_population_16_years_and_over_in_labor_force_civilian_labor_force_employed + percent_hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_white_alone + percent_households_by_type_households_with_one_or_more_people_65_years_and_over + percent_educational_attainment_percent_bachelors_degree_or_higher + percent_ancestry_total_population_german + percent_educational_attainment_population_25_years_and_over_bachelors_degree + percent_income_and_benefits_in_2016_inflation_adjusted_dollars_with_social_security + percent_ancestry_total_population_irish + percent_educational_attainment_population_25_years_and_over_less_than_9th_grade + percent_employment_status_population_16_years_and_over_not_in_labor_force + percent_employment_status_population_16_years_and_over_in_labor_force + percent_race_one_race_black_or_african_american + percent_sex_and_age_62_years_and_over + percent_hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_black_or_african_american_alone + percent_race_race_alone_or_in_combination_with_one_or_more_other_races_total_population_black_or_african_american, data = SortData2)

summary(fit) 

fit2 <- stepAIC(fit, direction="backward")

Step4 <- data.frame(summary(fit2)$coefficients)

write.csv(Step4, file = "C:/Users/drewc/OneDrive - University of Florida/Spring 2019/PHC6937/Course Project/Step4FL.csv")
