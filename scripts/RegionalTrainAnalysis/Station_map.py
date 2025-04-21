import pandas as pd
import folium
from Overland import add_overland_line

excel_path = r"C:\Academic\Aus_Trains\data\Processed_Data\RailwayInfo.xlsx"
stations_df = pd.read_excel(excel_path, sheet_name='Stations')
#Imports the processed data set

m = folium.Map(location=[-25.2744, 133.7751], zoom_start =5)
# This creates the Australian Map

for index, row in stations_df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Station_name'],
        tooltip=row['Station_name'],
    ).add_to(m)
# Creation of the markers in the given railway station locations
add_overland_line(m, stations_df, excel_path)

m.save("Australian_Railway_Stations.html")