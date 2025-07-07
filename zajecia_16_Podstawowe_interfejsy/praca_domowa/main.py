import requests
from file_handler import FileHandler
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim


file_handler = FileHandler(file_path="data.json")

def get_weather_for_country(latitude, longitude, searched_date):
    url = (f"https://api.open-meteo.com/v1/forecast?"
           f"latitude={latitude}&longitude={longitude}&hourly=rain"
           f"&daily=rain_sum&timezone=Europe%2FLondon"
           f"&start_date={searched_date}&end_date={searched_date}")
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Błąd zapytania do API.")
        return None

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

def get_coordinates(location_name):
    geolocator = Nominatim(user_agent="open_meteo_app")
    location = geolocator.geocode(location_name)
    if location:
        return location.latitude, location.longitude
    else:
        print("Nie udało się znaleźć współrzędnych dla podanej lokalizacji.")
        return None, None

def interpret_rain_sum(rain_sum):
    if rain_sum is None or rain_sum < 0:
        return "Nie wiem"
    elif rain_sum == 0.0:
        return "Nie będzie padać"
    else:
        return "Będzie padać"

def main():

    user_date = input("Podaj datę (YYYY-MM-DD). Jeśli nie podasz, zostanie użyta data jutrzejsza: ").strip()
    if not user_date:
        user_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(user_date, "%Y-%m-%d")
        except ValueError:
            print("Błędny format daty. Użyj formatu YYYY-MM-DD.")
            return


    location_name = input("Podaj nazwę lokalizacji (np. Warszawa, Poland): ").strip()
    if not location_name:
        print("Nie podano lokalizacji.")
        return


    if user_date in file_handler.data:
        print("Dane już są zapisane. Pobieram z pliku...")
        rain_sum = file_handler.data[user_date].get("rain_sum")
    else:
        latitude, longitude = get_coordinates(location_name)
        if latitude is None or longitude is None:
            return

        response_data = get_weather_for_country(latitude, longitude, user_date)
        if not response_data:
            print("Nie udało się pobrać danych pogodowych.")
            return

        modify_data_from_get_weather_for_country(response_data, file_handler, user_date)
        rain_sum = file_handler.data[user_date].get("rain_sum")

    wynik = interpret_rain_sum(rain_sum)
    print(f"\n Data: {user_date}\n Lokalizacja: {location_name}\n Prognoza: {wynik}")

if __name__ == "__main__":
    main()
