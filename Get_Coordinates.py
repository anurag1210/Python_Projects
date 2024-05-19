import requests
import certifi

def get_geolocation(address):
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': address,
        'format': 'json',
        'limit': 1
    }

    # Make a request to the Nominatim API
    response = requests.get(url, params=params, verify=certifi.where())

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if data:
            # Extract the latitude and longitude
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return latitude, longitude
        else:
            return None, None
    else:
        print(f"Error: Unable to get geolocation (status code {response.status_code})")
        return None, None

# Replace with your address
address = "77 Colehill Crescent, BH9 3RA"
latitude, longitude = get_geolocation(address)

if latitude and longitude:
    print(f"The geolocation of '{address}' is:")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print("Geolocation could not be determined.")
