## Prep Code

setwd("C:/Users/drewc/Documents/healthy_neighborhoods")

library(ggmap)
library(ggplot2)
library(acs)
library(tigris)
library(leaflet)

register_google(key = "AIzaSyA9EoExZadzR60Oy6xnL_nDJ8wgNksxKNI", write = TRUE)
api.key.install(key = "f6d68b9d7fc73bc998b16776f37836fbd4f187f8")

# Get FL Census Tract Map

hdat = read.csv("rf/rf_data_50acs.csv")

fl = tracts(state = "FL")

plot(fl)

## Combine with Health Outcome Data

dm = read.csv("maps/maps_data_dmct.csv")

fldm = geo_join(fl, dm, "GEOID", "GEOID")

## Create Map

leaflet() %>% addPolygons(data = fldm, fillColor = "blue")
