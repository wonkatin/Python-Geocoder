import requests
import geocoder
from secrets import API_KEY


API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

destinations = [
  "Space Needle",
  "Crater Lake",
  "Golden Gate Bridge",
  "Yosemite National Park",
  "Las Vegas, Nevada",
  "Grand Canyon National Park",
  "Aspen, Colorado",
  "Mount Rushmore",
  "Yellowstone National Park",
  "Sandpoint, Idaho",
  "Banff National Park",
  "Capilano Suspension Bridge",
]

for destination in destinations:
  lat, lng = geocoder.arcgis(destination).latlng
  result = requests.request('GET', f"{API_BASE_URL}?lat={lat}&lon={lng}&appid={API_KEY}").json()
  weather_description = result["weather"][0]["description"]
  kelvin = result["main"]["temp"]
  temperature = (kelvin - 273.15) * 9 / 5 + 32


  print(f"{destination} is located at ({lat}, {lng})")
  print(f"At {destination} right now, it's {weather_description} with a temperature of {temperature:.1f}°F\n")
