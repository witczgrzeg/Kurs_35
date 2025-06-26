import requests
from file_handler import FileHandler
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim


# ======= 1. Inicjalizacja obiektu do zapisu/odczytu =======
file_handler = FileHandler(file_path="data.json")


# ======= 2. Funkcja pobierająca dane pogodowe =======
def get_weather_for_country(latitude, longitude, searched_date):
    url = (f"https://api.open-meteo.com/v1/forecast?"
           f"latitude={latitude}&longitude={longitude}"
           f"&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon"
           f"&start_date={searched_date}&end_date={searched_date}")
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Podana wartość jest niewłaściwa, spróbuj jeszcze raz")
        return None


# ======= 3. Funkcja modyfikująca dane i zapisująca je =======
def modify_data_from_get_weather_for_country(response_data, file_handler_, searched_date):
    latitude = response_data.get("latitude")
    longitude = response_data.get("longitude")
    rain_sum = None
    if "daily" in response_data and "rain_sum" in response_data["daily"]:
        rain_list = response_data["daily"]["rain_sum"]
        if rain_list:
            rain_sum = rain_list[0]
    result = {
        "latitude": latitude,
        "longitude": longitude,
        "rain_sum": rain_sum
    }
    file_handler_.data[searched_date] = result
    file_handler_.write_data_to_file()


# ======= 4. Funkcja geokodująca miasto na współrzędne =======
def get_coordinates(location_name):
    geolocator = Nominatim(user_agent="twoja_aplikacja")
    location = geolocator.geocode(location_name)
    if location:
        return location.latitude, location.longitude
    else:
        print("Nie udało się znaleźć współrzędnych dla podanej lokalizacji.")
        return None, None


# ======= 5. Główna logika programu z input() =======
location_name = input("Podaj nazwę miasta (np. 'Warsaw'): ").strip()
if not location_name:
    print("Nie podano miasta – spróbuj ponownie.")
    exit(1)

searched_date = input("Podaj datę w formacie RRRR-MM-DD (lub zostaw puste, by użyć jutrzejszej): ").strip()
if not searched_date:
    searched_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

latitude, longitude = get_coordinates(location_name)

if latitude is not None and longitude is not None:
    response_data = get_weather_for_country(latitude, longitude, searched_date)
    if response_data:
        modify_data_from_get_weather_for_country(response_data, file_handler, searched_date)

        # ⬇️ Dodaj od tej linii:
        rain_sum = response_data.get("daily", {}).get("rain_sum", [None])[0]
        if rain_sum is None or rain_sum < 0:
            rain_info = "Nie wiem"
        elif rain_sum == 0.0:
            rain_info = "Nie będzie padać"
        else:
            rain_info = "Będzie padać"

        print(f"\n✅ Dane pogodowe zostały zapisane dla lokalizacji: {location_name} na dzień {searched_date}.")
        print(f"📍 Współrzędne: {latitude}, {longitude}")
        print(f"🌧️ Suma opadów: {rain_sum} mm")
        print(f"📝 Prognoza: {rain_info}")

