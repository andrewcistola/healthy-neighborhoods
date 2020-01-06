#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Neville Subproject: Using Random Forestes, Factor Analysis, and Recursive Feature Selection to Screen Variables for Imapcts on Public Health
## Florida Charts Census Tract Mortality Data: The R Project for Statistical Computing Code Script by DrewC!

### Step 1: Import Libraries and Import Dataset

library(tidverse)
library(tigris)
library(leaflet)
library(mapview)

setwd("C:/Users/drewc/Documents/healthy_neighborhoods")

# Get FL Census Tract Map

fl = tracts(state = "FL")

## Combine with Data

dm = read.csv("maps/maps_data_dmct.csv") # Create excel with GEOID, health outcome and selected variable

fldm = geo_join(fl, dm, "GEOID", "GEOID")

## Create Map for Health Outcome

pal1 <- colorNumeric("Greens", domain = c(0, 120))

dmap <- leaflet() %>% addPolygons(data = fldm, 
                          fillColor = ~pal1(fldm$Diabetes.Mellitus),
                          fillOpacity = 0.7, 
                          weight = 0.2, 
                          smoothFactor = 0.2) %>%
  addLegend(pal = pal, 
            values = fldm$Diabetes.Mellitus, 
            position = "bottomright", 
            title = "Diabetes Deaths by Census Tract in Florida")

mapshot(dmap, file = "maps/dmap.jpeg")

## Create Map for Social Vairable

pal2 <- colorNumeric("Blues", domain = c(0, 120))

colmap <- leaflet() %>% addPolygons(data = fldm, 
                          fillColor = ~pal2(fldm$College.Educated),
                          fillOpacity = 0.7, 
                          weight = 0.2, 
                          smoothFactor = 0.2) %>%
  addLegend(pal = pal, 
            values = fldm$Diabetes.Mellitus, 
            position = "bottomright", 
            title = "College Educated by Census Tract in Florida")

mapshot(colmap, file = "maps/colmap.jpeg")
