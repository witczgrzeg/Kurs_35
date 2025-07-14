import json
import os
import requests
from geopy.geocoders import Nominatim

class WeatherForecast:
    def __init__(self, file_path="data.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False)
        self.data = self._load_data()
        self._iter_keys = None

    def _load_data(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_data(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def get_coordinates(self, location_name):
        geolocator = Nominatim(user_agent="open_meteo_app")
        location = geolocator.geocode(location_name)
        if location:
            return location.latitude, location.longitude
        else:
            print("Nie znaleziono lokalizacji.")
            return None, None

    def fetch_weather(self, latitude, longitude, date):
        url = (f"https://api.open-meteo.com/v1/forecast?"
               f"latitude={latitude}&longitude={longitude}&hourly=rain"
               f"&daily=rain_sum&timezone=Europe%2FLondon"
               f"&start_date={date}&end_date={date}")
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            rain = data.get("daily", {}).get("rain_sum", [None])[0]
            return rain
        else:
            print("Błąd pobierania danych z API.")
            return None

    def __getitem__(self, key):
        # key = (city, date)
        city, date = key
        return self.data.get(city, {}).get(date, None)

    def __setitem__(self, key, value):
        # key = (city, date), value = "Będzie padać"
        city, date = key
        if city not in self.data:
            self.data[city] = {}
        self.data[city][date] = value
        self._save_data()

    def __iter__(self):
        # iterator po wszystkich datach występujących w danych (unikalne daty)
        all_dates = set()
        for city_data in self.data.values():
            all_dates.update(city_data.keys())
        self._iter_keys = iter(sorted(all_dates))
        return self

    def __next__(self):
        if self._iter_keys is None:
            self.__iter__()
        return next(self._iter_keys)

    def items(self):
        # generator zwracający (data, opis_pogody) ze wszystkich miast i dat
        for city_data in self.data.values():
            for date, forecast in city_data.items():
                yield date, forecast
