#call weather api and return forcast 
#https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API key}

from ast import parse
import imp
from urllib import response
import requests
import urllib.parse
import time
import datetime
from datetime import date

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
    #print(loc_info[0])

    api_add='https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(loc_info[0],loc_info[1],key)
    requests.get(api_add)
    
#{"coord":{"lon":-81.3145,"lat":29.8947},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"base":"stations","main":{"temp":297.56,"feels_like":298.25,"temp_min":295.93,"temp_max":299.31,"pressure":1013,"humidity":84},"visibility":10000,"wind":{"speed":5.66,"deg":160},"clouds":{"all":40},"dt":1648070303,"sys":{"type":1,"id":5825,"country":"US","sunrise":1648034725,"sunset":1648078686},"timezone":-14400,"id":4170894,"name":"Saint Augustine","cod":200}
    






def main():
    api_add='https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'
    key='d9f364914229889d68ce44400d7e7c9d'
    
    loc_info=getLocation()
    unix_datetime=getDateTime()
    weather_data=callWeather(loc_info,unix_datetime,key)
   






if __name__=="__main__":
    main()

