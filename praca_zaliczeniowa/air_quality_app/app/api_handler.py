import requests
from geopy.geocoders import Nominatim

BASE_URL = "https://api.openaq.org/v3"
API_KEY = "9842cf2ba34018b9ff7e2f1593819e26e814a4f71f0001e65bf688f92e25c865"

geolocator = Nominatim(user_agent="air_quality_app")

def geocode_city(city_name):
    """Zwraca (latitude, longitude) dla podanej nazwy miasta/regionu."""
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    return None, None

def get_latest_data_by_coords(latitude, longitude, radius_km=10):
    """Pobiera najnowsze dane jakości powietrza z OpenAQ dla współrzędnych."""
    url = f"{BASE_URL}/latest"
    params = {
        "coordinates": f"{latitude},{longitude}",
        "radius": radius_km * 1000,  # w metrach
        "limit": 100
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 410:
            return {"error": "Dane dla podanych współrzędnych są niedostępne (410 Gone)."}
        else:
            raise
