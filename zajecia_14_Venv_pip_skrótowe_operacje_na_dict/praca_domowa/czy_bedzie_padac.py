"""
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

Komentarze:
Brak komentarzy

"""
import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry


latitude = 53.3498  # Example latitude for Dublin
longitude = -6.2603 # Example longitude for Dublin
city = get_city_from_coordinates(latitude, longitude)

if city:
    print(f"The city for coordinates ({latitude}, {longitude}) is: {city}")
else:
    print(f"Could not find city for coordinates ({latitude}, {longitude})")


