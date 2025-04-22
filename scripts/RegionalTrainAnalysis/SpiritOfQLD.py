import pandas as pd
import folium

def add_spirit_line(m, stations_df, excel_path):
    df = pd.read_excel(excel_path, sheet_name="Spirit of QLD").sort_values(by="Order")

    route_coords=[]

    for station in df['Station_name']:
        match = stations_df[stations_df['Station_name'].str.contains(station)]
        if not match.empty:
            lat = match.iloc[0]['Latitude']
            lon = match.iloc[0]['Longitude']
            route_coords.append((lat, lon))
        else:
            print(f"Station not found: {station}")

    folium.PolyLine(
        locations=route_coords,
        color='red',
        opacity=1,
        tooltip="Spirit of QLD",
    ).add_to(m)

    for coord, name in zip(route_coords, df['Station_name']):
        folium.Marker(
            location=coord,
            popup=name,
            icon=folium.Icon(color='red', icon="map-marker", prefix="fa")
        ).add_to(m)
