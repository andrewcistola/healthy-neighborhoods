# Prep Code

import os
import pandas as pnd
import numpy as np
import folium

os.chdir("C:/Users/drewc/Documents/healthy_neighborhoods")

# Get Map of FL

map_fl = folium.Map(location = [51.5074, 0.1278], 
                    tiles = "Stamen Toner",
                    zoom_start = 11)
