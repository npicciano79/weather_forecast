#call weather api and return forcast 
#https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API key}

from argparse import Namespace
import requests
import urllib.parse
import time
from datetime import datetime,date
import json
import tkinter as tk 

def mainDisplay(location,description,fahern_data,date_time):

    #set location datetime
    loc_dateTime='The current forecast for {} on {} is: '.format(location,date_time)
   
    r=tk.Tk()
    r.geometry('400x400')
    r.title('Weather Display')
    text_font=('Helvetica',30,'bold')
    background='#add8e6'

    #create frames
    main_frame=tk.Frame(r,bg=background)
    main_frame.place(relx=0,rely=0,relwidth=1,relheight=1)

    #add labels to frames
    location_label=tk.Label(main_frame,text=loc_dateTime)
    location_label.place(relx=0,rely=0,relwidth=1,relheight=0.25)

    currTemp_label=tk.Label(main_frame,text='Current Temp: {}'.format(fahern_data[0]))
    currTemp_label.place(relx=0,rely=0.25,relwidth=0.5,relheight=0.25)

    dailyLow_label=tk.Label(main_frame,text='Daily low: {}'.format(fahern_data[2]))
    dailyLow_label.place(relx=0,rely=0.5,relwidth=0.5,relheight=0.25)

    dailyHigh_label=tk.Label(main_frame,text='Daily High: {}'.format(fahern_data[3]))
    dailyHigh_label.place(relx=0,rely=.75,relwidth=0.5,relheight=0.25)

    forecastIll_label=tk.Label(main_frame,text='#')
    forecastIll_label.place(relx=0.5,rely=0.25,relwidth=0.5,relheight=0.5)


    r.mainloop()

    



    






#get lattitude and longitude from town/city
def getLocation(city):
    country = "USA"
    url = "https://nominatim.openstreetmap.org/?addressdetails=1&q=" + city + "+" + country +"&format=json&limit=1"
    response = requests.get(url).json()
    if response==[]:
        city=input("Invalid Entry, please reenter the city name: ")
        getLocation(city)
    else:    
        lat=response[0]["lat"]
        lon=response[0]["lon"]
        location=response[0]['display_name']
        loc_info=[lat,lon,location]
    return loc_info
    
#get datetime in unix format
def getDateTime():
    #get month name, day hour and minute
    now=datetime.now().strftime("%B %d, %H:%M")
    #split now into monday/day, hour , minute 
    monthday=now.split(',')[0]
    hour_min=now.split(', ')[1]
    hour=int(hour_min.split(':')[0])
    min=hour_min.split(':')[1]
      
    #convert hour from military time
    setting="PM"
    if hour>12:
        hour=hour-12
    else:
        setting='AM'
   
    #concat Month, day hour minute 
    date_time='{} at {}:{} {}'.format(monthday,str(hour),min,setting)   
    
    #calulate unix datetime needed for weather API
    unix_time=time.time()
    return unix_time,date_time



def callWeather(loc_info,key):
    api_add='https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(loc_info[0],loc_info[1],key)
    raw_data = requests.get(api_add).json()
    return raw_data
    

#need to parse data and display correctly 
def getData(raw_data):
    data_request=['weather','main']
    data_get=[]
    count=0
    value = Namespace(**raw_data)
    #for key,value in raw_data.items():
       # if key in data_request:
    description=str(value.weather).split('description')[1].split(',')[0].replace(':'," ").replace("'",'')
    #print(value.main)
    main_key=['temp','feels_like','temp_min','temp_max','humidity']
    main_data=[]
    for key,val in value.main.items():
        if key in main_key:
            main_data.append(val)
    
    return description,main_data

def convertTemp(main_data):
    
    for i in range(0,len(main_data)-1):
        main_data[i]=((main_data[i]-273.15)*9)//5+32
    
    return main_data

def formatData(fahern_data):
    super='o'
    current_temp=(f"{fahern_data[0]}\N{DEGREE SIGN}")
    min_temp=(f"{fahern_data[2]}\N{DEGREE SIGN}")
    max_temp=(f"{fahern_data[3]}\N{DEGREE SIGN}")
    #print("""The weather for {} today, {} is: \nThere are{}s\nCurrent Temperature:{}\nMinimum Temperature:{}\nMaximum Temperature:{}\nHumidity:{}%"""
    #.format(city.title(),date_time,description,current_temp,min_temp,max_temp,fahern_data[4]))

    return current_temp,min_temp,max_temp
    
    


    
#& c:/Users/npicc/Documents/python/python.exe c:/Users/npicc/Documents/Coding/projects/weatherDisplay/weatherDisplay.py
        

    



def main():
    #api_add='https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'
    key='d9f364914229889d68ce44400d7e7c9d'
    location='St. Augustine, Florida'
    loc_info=['29.8946952', '-81.3145395']
    #get location and longitute/latitude
    #city=input("Enter the city you would like to find the temperature of: ")
    #loc_info=getLocation('st augustine')
    
    #get current datetime
    unix_time,date_time=getDateTime()

    #call weatherAPI, passes loc_info, time/date,key
    raw_data=callWeather(loc_info,key)
    description,main_data=getData(raw_data)
    fahern_data=convertTemp(main_data)
    current_temp,min_temp,max_temp=formatData(fahern_data)
    mainDisplay(location,description,fahern_data,date_time)





if __name__=="__main__":    
    main()

