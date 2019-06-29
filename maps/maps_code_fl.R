## Prep Code

setwd("C:/Users/drewc/Documents/healthy_neighborhoods")

library(ggmap)
library(ggplot2)
library(maps)

register_google(key = "AIzaSyA9EoExZadzR60Oy6xnL_nDJ8wgNksxKNI", write = TRUE)

# Get FL Map

hdat = read.csv("rf/rf_data_50acs.csv")

fl = map_data("state", region = "florida")

ggplot() + geom_polygon(data = fl, aes(long, y = lat, group = group)) + coord_quickmap()

