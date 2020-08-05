import requests
import geocoder
from api import DS_API_URL

destinations = ["The Space Needle",
  "Crater Lake",
  "The Golden Gate Bridge",
  "Yosemite National Park",
  "Las Vegas, Nevada",
  "Grand Canyon National Park",
  "Aspen, Colorado",
  "Mount Rushmore",
  "Yellowstone National Park",
  "Sandpoint, Idaho",
  "Banff National Park",
  "Capilano Suspension Bridge"]

for point in destinations:
  # Get the latitude and longitude from `geocoder`.
  loc = geocoder.arcgis(point)
  result = requests.request('GET', f'{DS_API_URL}{loc.latlng[0]},{loc.latlng[1]}').json()['currently']

  # Print out `geopy`'s results.
  print("{0} is located at ({1:.4f}, {2: .4f})".format(point, loc.latlng[0], loc.latlng[1]))
  print("At {0} right now, it's {1} with a temperature of {2: .1f}ºf".format(point, result["summary"], result['temperature']))