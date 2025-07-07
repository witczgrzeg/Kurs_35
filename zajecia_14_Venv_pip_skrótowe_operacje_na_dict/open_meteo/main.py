"""
Zadanie - obsługa biblioteki zewnętrznej
Arrow down
Napisz program, który sprawdzi, czy danego dnia będzie padać. Użyj do tego poniższego API. Aplikacja ma działać następująco:

Program pyta dla jakiej daty należy sprawdzić pogodę. Data musi byc w formacie YYYY-mm-dd, np. 2022-11-03. W przypadku nie podania daty, aplikacja przyjmie za poszukiwaną datę następny dzień.
Aplikacja wykona zapytanie do API w celu poszukiwania stanu pogody.
Istnieją trzy możliwe informacje dla opadów deszczu:
Będzie padać (dla wyniku większego niż 0.0)
Nie będzie padać (dla wyniku równego 0.0)
Nie wiem (gdy wyniku z jakiegoś powodu nie ma lub wartość jest ujemna)
Będzie padać
Nie będzie padać
Nie wiem
Wyniki zapytań powinny być zapisywane do pliku. Jeżeli szukana data znajduje sie juz w pliku, nie wykonuj zapytania do API, tylko zwróć wynik z pliku.

URL do API:
https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}

W URL należy uzupełnić parametry: latitude, longitude oraz searched_date

"""

import requests
from file_handler import FileHandler
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim




file_handler = FileHandler(file_path="data.json")

def get_weather_for_country(latitude, longitude, searched_date):
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}")
    response = requests.get(url=url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("Podana wartość jest niewłaściwa, spróbuj jeszcze raz")
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
    geolocator = Nominatim(user_agent="twoja_aplikacja")
    location = geolocator.geocode(location_name)
    if location:
        return location.latitude, location.longitude
    else:
        print("Nie udało się znaleźć współrzędnych dla podanej lokalizacji.")
        return None, None

