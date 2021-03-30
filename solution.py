import geocoder

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
  print(f"{destination} is located at ({lat}, {lng})")
