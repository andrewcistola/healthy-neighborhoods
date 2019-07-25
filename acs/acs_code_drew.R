---
title: "American Community Survey"
author: "Andrew Cistola"
date: "June 17, 2019"
output: html_document
---


library(tibble)
library(dplyr)

setwd("C:/Users/drewc/Downloads")

Social <- read.csv("ACS_16_5YR_DP02_with_ann.csv")
Economic <- read.csv("ACS_16_5YR_DP03_with_ann.csv")
Housing <- read.csv("ACS_16_5YR_DP04_with_ann.csv")
Demographic <- read.csv("ACS_16_5YR_DP05_with_ann.csv")

se = inner_join(Social, Economic, by = "GEO.id")
seh = inner_join(se, Housing, by = "GEO.id")
acs = inner_join(seh, Demographic, by = "GEO.id")

write.csv(acs, "C:/Users/drewc/Documents/GitHub/stories/data/acs_data_raw.csv")
