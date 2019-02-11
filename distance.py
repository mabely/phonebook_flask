import sqlite3
import json 
import requests
from math import pi, sin, cos, sqrt, atan2

#currentLat = 51.486879
#currentLon = -0.091014
#print(getBusinessByType("EC3M 1AA", "Shoes"))


def distance(lat1, lng1, lat2, lng2): 
    #return distance as meter if you want km distance, remove "* 1000" 
    radius = 6371

    dLat = (lat2-lat1) * pi/180 
    dLng = (lng2-lng1) * pi/180 

    lat1 = lat1 * pi/180 
    lat2 = lat2 * pi/180 

    val = sin(dLat/2) * sin(dLat/2) + sin(dLng/2) * sin(dLng/2) * cos(lat1) * cos(lat2)  
    ang = 2 * atan2(sqrt(val), sqrt(1-val)) 
    return round(radius * ang,2)

#print(distance(currentLat, currentLon, lat1, lng1),"km")
