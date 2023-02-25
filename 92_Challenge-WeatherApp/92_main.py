# Day 92 on Replit: "Challenge: Weather app"

# pip install geopy

import requests
import json
from datetime import date
from geopy.geocoders import Nominatim
import os

geo = Nominatim(user_agent="myApp")
place = input("Introduce a city: ")
loc = geo.geocode(place)


# test data
timezone = "GMT"
latitude = loc.latitude
longitude = loc.longitude

response = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

weather = response.json()

# print(json.dumps(weather, indent=2))


def find_weather(code):
    if code == 0:
        return "Clear sky"
    elif code == 1 or code == 2 or code == 3:
        return "Mainly clear, partly cloudy, and overcast"
    elif code == 45 or code == 48:
        return "Fog and depositing rime fog"
    elif code == 51 or code == 53 or code == 55:
        return "Drizzle: Light, moderate, and dense intensity"
    elif code == 56 or code == 57:
        return "Freezing Drizzle: Light and dense intensity"
    elif code == 61 or code == 63 or code == 65:
        return "Rain: Slight, moderate and heavy intensity"
    elif code == 66 or code == 67:
        return "Freezing Rain: Light and heavy intensity"
    elif code == 71 or code == 73 or code == 75:
        return "Snow fall: Slight, moderate, and heavy intensity"
    elif code == 77:
        return "Snow grains"
    elif code == 80 or code == 81 or code == 82:
        return "Rain showers: Slight, moderate, and violent"
    elif code == 85 or code == 86:
        return "Snow showers slight and heavy"
    elif code == 95:
        return "Thunderstorm: Slight or moderate"
    else:
        return "Thunderstorm with slight and heavy hail"


weather_code = weather["daily"]["weathercode"][0]
max = weather["daily"]["temperature_2m_max"][0]
min = weather["daily"]["temperature_2m_min"][0]


os.system("cls")

print(f"Weather in {loc}")
print(find_weather(weather_code))
print(f"🔥 = {max}     ❄ = {min}")
