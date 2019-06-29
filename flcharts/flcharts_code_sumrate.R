library(dplyr)

setwd("C:/Users/drewc/Documents/healthy_neighborhoods")

pop <- read.csv("acs/acs_data_pop.csv")
flch <- read.csv("flcharts/flcharts_data_50totalsum.csv")

join = inner_join(pop, flch, by = "Tract")

write.csv(join, "C:/Users/drewc/Documents/healthy_neighborhoods/flcharts/flcharts_data_50rate.csv")


