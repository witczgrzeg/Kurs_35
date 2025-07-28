import requests

BASE_URL = "https://api.openaq.org/v2"

def get_latest_data(city):
    response = requests.get(f"{BASE_URL}/latest", params={"city": city})
    response.raise_for_status()
    return response.json()
