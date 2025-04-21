import pandas as pd
import folium

df = pd.read_excel(r"C:\Academic\Aus_Trains\data\Processed_Data\RailwayInfo.xlsx")
#Imports the processed data set

m = folium.Map(location=[-25.2744, 133.7751], zoom_start =5)
# This creates the Australian Map

for index, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Station_name'],
        tooltip=row['Station_name'],
    ).add_to(m)
# Creation of the markers in the given railway station locations
m.save("Australian_Railway_Stations.html")