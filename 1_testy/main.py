import asyncio
from datetime import datetime
from geopy.geocoders import Nominatim
from openaq import AsyncOpenAQ
from file_handler import FileHandler

API_KEY = "9842cf2ba34018b9ff7e2f1593819e26e814a4f71f0001e65bf688f92e25c865"
DATA_FILE = "data.json"

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="moja_aplikacja")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        raise ValueError(f"Nie znaleziono współrzędnych dla miasta: {city_name}")

def parse_measurement_date(m):
    try:
        return datetime.fromisoformat(m.period.datetime_from.local)
    except Exception:
        return None

def format_date(dt):
    return dt.strftime("%d.%m.%Y %H:%M")

async def fetch_latest_measurement_for_sensor(client, sensor_id):
    response = await client.measurements.list(sensors_id=sensor_id, limit=100)
    if not response.results:
        return None
    valid = [(m, parse_measurement_date(m)) for m in response.results]
    valid = [pair for pair in valid if pair[1] is not None]
    if not valid:
        return None
    latest, latest_date = sorted(valid, key=lambda x: x[1])[-1]
    return latest, latest_date

async def main():
    handler = FileHandler(DATA_FILE)
    city = input("Podaj nazwę miasta: ").strip()

    try:
        lat, lon = get_coordinates(city)
        print(f"Współrzędne {city}: {lat}, {lon}")

        async with AsyncOpenAQ(api_key=API_KEY) as client:
            locations = await client.locations.list(coordinates=[lat, lon], radius=10000, limit=10)
            if not locations.results:
                print("Brak lokalizacji w pobliżu.")
                return

            print(f"Lokalizacje najbliżej {city}:")

            city_data = {"locations": {}}

            for loc in locations.results:
                print(f"ID: {loc.id}, Nazwa: {loc.name}, Odległość: {round(loc.distance, 2)} m")

                sensors = getattr(loc, "sensors", [])
                if not sensors:
                    print("  Brak sensorów dla tej lokalizacji.")
                    continue

                latest_measurement = None
                latest_date = None
                latest_sensor_id = None

                # Znajdź najnowszy pomiar spośród wszystkich sensorów lokalizacji
                for sensor in sensors:
                    latest_data = await fetch_latest_measurement_for_sensor(client, sensor.id)
                    if latest_data is None:
                        print(f"  Brak pomiarów dla sensora ID {sensor.id}.")
                        continue
                    latest, date = latest_data
                    if latest_date is None or date > latest_date:
                        latest_date = date
                        latest_measurement = latest
                        latest_sensor_id = sensor.id

                if latest_measurement is None:
                    print("  Brak ważnych pomiarów dla lokalizacji.")
                    continue

                date_str = format_date(latest_date)
                param = getattr(latest_measurement.parameter, "name", str(latest_measurement.parameter)).upper()
                units = getattr(latest_measurement.parameter, "units", "")
                value_str = f"{param}: {latest_measurement.value} {units}"

                print(f"  Najnowszy pomiar sensor ID {latest_sensor_id} - {value_str} (data: {date_str})")

                city_data["locations"][str(loc.id)] = {
                    "name": loc.name,
                    "distance": round(loc.distance, 2),
                    "measurements": {
                        f"sensor_{latest_sensor_id}": {
                            "date": date_str,
                            "value": value_str
                        }
                    }
                }

            # Zapis do pliku
            handler.data[city] = city_data
            handler.write_data_to_file()

            print(f"\nZapisane dane w {DATA_FILE}:")
            for loc_id, loc_info in city_data["locations"].items():
                print(f"Lokalizacja {loc_id} ({loc_info['name']}):")
                for sensor_id, meas in loc_info["measurements"].items():
                    print(f"  {sensor_id} | {meas['date']} | {meas['value']}")

    except Exception as e:
        print("Błąd:", e)

if __name__ == "__main__":
    asyncio.run(main())
