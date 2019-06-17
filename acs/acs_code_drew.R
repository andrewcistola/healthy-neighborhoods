---
title: "American Community Survey"
author: "Andrew Cistola"
date: "June 17, 2019"
output: html_document
---


library(tibble)
library(dplyr)

setwd("C:/Users/drewc/Documents/Data")

Social <- read.csv("ACS_17_5YR_DP02_with_ann.csv")
Economic <- read.csv("ACS_17_5YR_DP03_with_ann.csv")
Housing <- read.csv("ACS_17_5YR_DP04_with_ann.csv")
Demographic <- read.csv("ACS_17_5YR_DP05_with_ann.csv")

se = inner_join(Social, Economic, by = "GEO.id")
seh = inner_join(se, Housing, by = "GEO.id")
ACS = inner_join(seh, Demographic, by = "GEO.id")

write.csv(ACS, "C:/Users/drewc/Documents/Data/acs_data_master.csv")