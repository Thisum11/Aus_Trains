import pandas as pd
df = pd.read_excel("C:\Academic\Aus_Trains\data\Processed_Data\RailwayInfo.xlsx")
# Importing the excel file to python

print(df.head())
#Making sure the file is successfully imported.

print(df.info())
#For the assurance of the structure

print(df.duplicated(subset=['Latitude', 'Longitude']).sum())
# To check if there's any station mentioned twice in the data set
