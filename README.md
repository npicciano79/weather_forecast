"#weather_forecast"

Displays weather data for user entered city 
API call to https://openweathermap.org/current
API link : 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'

Program retrieves city name from user, passes to "https://nominatim.openstreetmap.org/?addressdetails=1&q=" to return logitude and latitude of city.  Asks user to reenter if not valid city 
getDateTime is called and returns unix datetime and current date time in format "Month day hour:minute"
Coordiantes, unixdatetime and key are passed to callWeather function which returns raw-data from openweathermap.org API
raw-date is passed to getData which parses raw_data returning description and temperature data
temperature data is passes to converTemp with converts data from kelvin to fahernite 
fahernite temp, description, city, and date time are passed to display data which formats the output



throws errors at special characters and numbers, need to fix


