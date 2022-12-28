#Plot points on the map.png and connect them with lines
from Functions import *
import folium 

def Plot_Map(Cities):

    print(Cities)
    Cities_Longitude_Latitude = Get_Longitude_Latitude()
    
    # Start Location
    Map = folium.Map(location=[30.4624974 , 31.184063 ], zoom_start=9)
    
    # Mark Cities
    for city in Cities:
        folium.Marker(location=Cities_Longitude_Latitude[city], popup=city, icon=folium.Icon(color='red', icon='info-sign')).add_to(Map)

    # Mark Start and End Cities
    folium.Marker(location=Cities_Longitude_Latitude[Cities[0]], popup=Cities[0], icon=folium.Icon(color='lightgreen', icon='info-sign')).add_to(Map)
    folium.Marker(location=Cities_Longitude_Latitude[Cities[-1]], popup=Cities[-1], icon=folium.Icon(color='lightred', icon='info-sign')).add_to(Map)

    # Draw Lines
    for key in range(len(Cities)-1):
        folium.PolyLine(locations=[Cities_Longitude_Latitude[Cities[key]],Cities_Longitude_Latitude[Cities[key+1]]], color="red", weight=5, opacity=0.8).add_to(Map)
        
    # Save Map
    Map.save('Map2.html')