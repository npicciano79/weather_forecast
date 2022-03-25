#call weather api and return forcast 
#https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API key}

from argparse import Namespace
from types import SimpleNamespace
from urllib import request, response
import requests
import urllib.parse
import time
import datetime
from datetime import date
import json

#get lattitude and longitude from town/city
def getLocation():
    city=input("Enter your city: ")
    country = "USA"
    url = "https://nominatim.openstreetmap.org/?addressdetails=1&q=" + city + "+" + country +"&format=json&limit=1"
    response = requests.get(url).json()
    lat=response[0]["lat"]
    lon=response[0]["lon"]
    location=response[0]['display_name']
    loc_info=[lat,lon,location]
    return loc_info

#get datetime in unix format
def getDateTime():
    presentDate = datetime.datetime.now()
    unix_datetime = datetime.datetime.timestamp(presentDate)*1000
    return unix_datetime

def callWeather(loc_info,unix_datetime,key):
    api_add='https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(loc_info[0],loc_info[1],key)
    raw_data = requests.get(api_add).json()
    return raw_data
    

#need to parse data and display correctly 
def displayData(raw_data):
    data_request=['weather','main']
    data_get=[]
    #value = Namespace(**raw_data)
    for key,value in raw_data.items():
        if key in data_request:
            input(raw_data[key])
            
    
    


    
#& c:/Users/npicc/Documents/python/python.exe c:/Users/npicc/Documents/Coding/projects/weatherDisplay/weatherDisplay.py
        

    



def main():
    api_add='https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'
    key='d9f364914229889d68ce44400d7e7c9d'
    
    loc_info=getLocation()
    unix_datetime=getDateTime()
    raw_data=callWeather(loc_info,unix_datetime,key)
    displayData(raw_data)
   






if __name__=="__main__":
    main()

"""
Namespace(coord={'lon': -81.3145, 'lat': 29.8947}, weather=[{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 
base='stations', main={'temp': 286.74, 'feels_like': 286.69, 'temp_min': 285.97, 'temp_max': 287.64, 'pressure': 1015, 'humidity': 97}, visibility=10000, wind={'speed': 1.54, 'deg': 230}, clouds={'all': 100}, dt=1648202781, sys={'type': 1, 'id': 5825, 'country': 'US', 'sunrise': 1648207378, 'sunset': 1648251557}, timezone=-14400, id=4170894, name='Saint Augustine', cod=200)
"""