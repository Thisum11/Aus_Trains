import pandas as pd
import folium

df = pd.read_excel(r"C:\Academic\Aus_Trains\data\Processed_Data\RailwayInfo.xlsx")
#Imports the processed data set

m = folium.Map(location=[-25.2744, 133.7751], zoom_start =5)
# This creates the Australian Map

m.save("Australian_Railway_Stations.html")