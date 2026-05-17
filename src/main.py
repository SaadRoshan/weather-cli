import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def display_weather(data):
    if data.get("cod") != 200:
        print(f"\n  Error: {data.get('message')}")
        return

    city_name = data["name"]
    country = data["sys"]["country"]
    condition = data["weather"][0]["description"].title()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print()
    print("=" * 35)
    print(f"  Weather in {city_name}, {country}")
    print("=" * 35)
    print(f"  Condition   : {condition}")
    print(f"  Temperature : {temp}°C")
    print(f"  Feels like  : {feels_like}°C")
    print(f"  Humidity    : {humidity}%")
    print(f"  Wind speed  : {wind} km/h")
    print("=" * 35)
    print()

city = input("Enter city name: ")
data = get_weather(city)
display_weather(data)