import folium
from folium.plugins import MarkerCluster
import pandas as pd
gtm = folium.Map(location=[0,0], zoom_start=1)
glaciers_DF = pd.read_csv("coord_spread.csv", encoding='iso-8859-1')
lat = list(glaciers_DF["LATITUDE"])
long = list(glaciers_DF["LONGITUDE"])
coord_List = []
for i in range(len(lat)):
    coord_List.append((lat[i], long[i]))
name_array = list(glaciers_DF["NAME"])

for i in range(0,len(coord_List), 10):
    folium.Marker(coord_List[i], popup=name_array[i] + " GLACIER", clustered_marker=True).add_to(gtm)

MarkerCluster(locations=coord_List).add_to(gtm)
gtm.save('gtm.html')
