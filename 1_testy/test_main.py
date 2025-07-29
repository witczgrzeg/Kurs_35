import asyncio
from datetime import datetime
from geopy.geocoders import Nominatim
from openaq import AsyncOpenAQ
from file_handler import FileHandler
import aiohttp

API_KEY = "9842cf2ba34018b9ff7e2f1593819e26e814a4f71f0001e65bf688f92e25c865"
DATA_FILE = "data.json"

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="moja_aplikacja")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        raise ValueError(f"Nie znaleziono współrzędnych dla miasta: {city_name}")

async def fetch_locations(client, lat, lon, radius=10000, limit=10):
    response = await client.locations.list(
        coordinates=[lat, lon],
        radius=radius,
        limit=limit
    )
    return response.results

async def fetch_measurements_for_sensor(client, sensor_id, limit=100):
    response = await client.measurements.list(
        sensors_id=sensor_id,
        limit=limit
    )
    return response.results

def parse_measurement_date(m):
    try:
        return datetime.fromisoformat(m.period.datetime_from.local)
    except Exception:
        return None

async def fetch_days_for_sensor(sensor_id, limit=30):
    url = f"https://api.openaq.org/v3/sensors/{sensor_id}/days"
    params = {
        "limit": limit,
        "order_by": "datetime",
        "sort": "desc"
    }
    headers = {
        "Authorization": f"Token {API_KEY}"
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, params=params) as resp:
            resp.raise_for_status()
            data = await resp.json()
            return data.get("results", [])


async def main():
    handler = FileHandler(DATA_FILE)
    city = input("Podaj nazwę miasta: ").strip()

    try:
        lat, lon = get_coordinates(city)
        print(f"Współrzędne {city}: {lat}, {lon}")

        async with AsyncOpenAQ(api_key=API_KEY) as client:
            locations = await fetch_locations(client, lat, lon)
            if not locations:
                print("Brak lokalizacji w pobliżu.")
                return

            locations_sorted = sorted(locations, key=lambda x: x.distance or float('inf'))

            print(f"Lokalizacje najbliżej {city}:")
            for loc in locations_sorted:
                print(f"ID: {loc.id}, Nazwa: {loc.name}, Odległość: {round(loc.distance, 2)} m")

            first_location = locations_sorted[0]
            sensors = first_location.sensors
            if not sensors:
                print("Brak sensorów dla tej lokalizacji.")
                return

            first_sensor = sensors[0]
            first_sensor_id = first_sensor.id
            parameter_name = first_sensor.parameter.name if hasattr(first_sensor.parameter, 'name') else str(first_sensor.parameter)
            parameter_units = first_sensor.parameter.units if hasattr(first_sensor.parameter, 'units') else ""

            print(f"\nPobieram pomiary dla sensora ID: {first_sensor_id} (parametr: {parameter_name})")

            measurements = await fetch_measurements_for_sensor(client, first_sensor_id)
            if not measurements:
                print("Brak pomiarów dla tego sensora.")
                return

            # Sparsuj daty pomiarów i wybierz najnowszy
            measurements_with_dates = [(m, parse_measurement_date(m)) for m in measurements]
            measurements_with_dates = [md for md in measurements_with_dates if md[1] is not None]

            if not measurements_with_dates:
                print("Brak poprawnych dat pomiarów.")
                return

            latest, latest_date = sorted(measurements_with_dates, key=lambda x: x[1])[-1]
            date_str = latest_date.strftime("%d.%m.%Y %H:%M")

            parameter = latest.parameter.name if hasattr(latest.parameter, "name") else str(latest.parameter)
            units = latest.parameter.units if hasattr(latest.parameter, "units") else ""

            print(f"\nNajnowszy pomiar dla {city}:")
            print(f"{parameter.upper()}: {latest.value} {units} (data: {date_str})")

            # zapis do pliku przez FileHandler
            handler[city, date_str] = f"{parameter.upper()}: {latest.value} {units}"

            # --- Pobranie danych dziennych (days) i zapis ---
            days_data = await fetch_days_for_sensor(first_sensor_id)
            if days_data:
                handler[f"sensor_{first_sensor_id}"] = days_data

            handler.write_data_to_file()

            # wyświetlenie dotychczasowych danych
            print(f"\nZapisane dane w {DATA_FILE}:")
            for c, d, val in handler.items():
                print(f"{c} | {d} | {val}")

    except Exception as e:
        print("Błąd:", e)

if __name__ == "__main__":
    asyncio.run(main())
