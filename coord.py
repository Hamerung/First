import requests
from coord_token import coord_token


def get_location():
    response = requests.get(f'http://api.ipapi.com/api/check?access_key={coord_token}')
    data = response.json()
       
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    return latitude, longitude

latitude, longitude = get_location()
print(f"Latitude: {latitude}, Longitude: {longitude}")
   