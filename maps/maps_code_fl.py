# Prep Code

import os
import pandas as pnd
import matplotlib.pyplot as plt
import folium

os.chdir("C:/Users/drewc/Documents/healthy_neighborhoods")

# Get Map of FL

map_fl = folium.Map(location = [51.5074, 0.1278], 
                    zoom_start = 11)
