import requests
import json
from datetime import datetime

def main():
    print("This is a weather app. It will tell you the current state and temperature for a city.")
    print("You can also check average temperature for tomorrow!")
    showWeather()

def showWeather():

    contination = True
    while contination:
        api_key = "d91a18cf8dd048738cd52804240906"

        city = input("Please input a city name: ")

        api_current_url = "http://api.weatherapi.com/v1/current.json?key=" + api_key + "&q=" + city

        response_current = requests.get(api_current_url)

        if response_current.status_code == 200:
            current_weather = response_current.json()

            condition = current_weather['current']['condition']['text']

            temp = float(current_weather['current']['temp_c'])

            print(f"It seems like the weather for {city} is {condition} and it is {temp}°C")
        else:
            print(f"Failed to fetch data. HTTP Status code: {response_current.status_code}")
        
        forecast = input("Would you like to know weather forecast for tomorrow? (y/n) ")
        
        days = str(2)

        api_forecast_url = "http://api.weatherapi.com/v1/forecast.json?key=" + api_key + "&q=" + city + "&days=" + days
        response_forecast = requests.get(api_forecast_url)


        if forecast == "y":
            if response_forecast.status_code == 200:
                forecast_weather = response_forecast.json()

                future_temp = float(forecast_weather['forecast']['forecastday'][1]['day']['avgtemp_c'])

                print(f"It seems like the average temperature tomorrow for {city} will be {future_temp}°C")
            else:
                print(f"Failed to fetch data. HTTP Status code: {response_forecast.status_code}")
        else:
            pass

        next_city = input("Would you like to check the weather for another city? (y/n) ")

        if next_city == "n":
            contination = False

if __name__ == '__main__':
    main()