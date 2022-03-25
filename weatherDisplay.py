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
    value = Namespace(**raw_data)
    print(value.weather)

    

        

    



def main():
    api_add='https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'
    key='d9f364914229889d68ce44400d7e7c9d'
    
    loc_info=getLocation()
    unix_datetime=getDateTime()
    raw_data=callWeather(loc_info,unix_datetime,key)
    displayData(raw_data)
   






if __name__=="__main__":
    main()

