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

## Combine with Data

dm = read.csv("maps/maps_data_dmct.csv")

fldm = geo_join(fl, dm, "GEOID", "GEOID")

## Create Map for Health Outcome

pal <- colorNumeric("Greens", domain = c(0, 120))

leaflet() %>% addPolygons(data = fldm, 
                          fillColor = ~pal(fldm$Diabetes.Mellitus),
                          fillOpacity = 0.7, 
                          weight = 0.2, 
                          smoothFactor = 0.2) %>%
  addLegend(pal = pal, 
            values = fldm$Diabetes.Mellitus, 
            position = "bottomright", 
            title = "Diabetes Deaths by Census Tract in Florida")

## Create Map for Social Vairable

pal2 <- colorNumeric("Blues", domain = c(0, 120))

leaflet() %>% addPolygons(data = fldm, 
                          fillColor = ~pal2(fldm$College.Educated),
                          fillOpacity = 0.7, 
                          weight = 0.2, 
                          smoothFactor = 0.2) %>%
  addLegend(pal = pal, 
            values = fldm$Diabetes.Mellitus, 
            position = "bottomright", 
            title = "College Educated by Census Tract in Florida")

