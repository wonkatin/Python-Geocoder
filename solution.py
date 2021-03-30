import geocoder 
import requests
from secrets import API_KEY
API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

destinations = [
    'Space Needle',
    'Crater Lake',
    'Golden Gate Bridge',
    'Yosemite National Park',
    'Las Vegas, Nevada',
    'Grand Canyon National Park',
    'Aspen, Colorado',
    'Mount Rushmore',
    'Yellowstone National Park',
    'Sandpoint, Idaho',
    'Banff National Park',
    'Capilano Suspension Bridge',
]

# result = geocoder.arcgis(destinations[0]).latlng
# print(result)
# for destination in destinations:
#     result = geocoder.arcgis(destination).latlng
#     print(f'{destination} is located at {result}')

# for destination in destinations:
#     banana1, banana2 = geocoder.arcgis(destination).latlng
#     print(f'{destination} is located at ({banana1}, {banana2})')


# for destination in destinations:
#     lat, lon = geocoder.arcgis(destination).latlng
#     print(f'{destination} is located at ({lat}, {lon})')

for point in destinations:
    lat, lon = geocoder.arcgis(point).latlng
    print(f'{point} is located at ({lat}, {lon})')
    full_api_url = f'{API_BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}'
    result = requests.request('GET', full_api_url).json()
    weather_description = result['weather'][0]['description']
    kelvin = result["main"]["temp"]
    temperature = (kelvin - 273.15) * 9 / 5 + 32
    print(f'At {point} right now, its {weather_description} with a temperature of {temperature:.1f}° F \n')   

  
    