import asyncio
from datetime import datetime
from geopy.geocoders import Nominatim
from openaq import AsyncOpenAQ
from file_handler import FileHandler
import aiohttp

API_KEY = "9842cf2ba34018b9ff7e2f1593819e26e814a4f71f0001e65bf688f92e25c865"
DATA_FILE = "data.json"

# Globalny klient
client: AsyncOpenAQ = None

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
    url = f"https://api.openaq.org/v2/sensors/{sensor_id}/days"
    params = {
        "limit": limit,
        "order_by": "datetime",
        "sort": "desc",
        "api_key": API_KEY
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            if resp.status == 200:
                json_data = await resp.json()
                return json_data.get("results", [])
            else:
                print(f"Błąd przy pobieraniu danych dniowych: HTTP {resp.status}")
                return []

async def get_air_quality_for_city(city):
    global client
    if client is None:
        client = AsyncOpenAQ(api_key=API_KEY)
        await client.__aenter__()  # ręczne otwarcie klienta, jak context manager

    handler = FileHandler(DATA_FILE)
    lat, lon = get_coordinates(city)

    locations = await fetch_locations(client, lat, lon)
    if not locations:
        return {"error": "Brak lokalizacji w pobliżu."}

    locations_sorted = sorted(locations, key=lambda x: x.distance or float('inf'))
    first_location = locations_sorted[0]
    sensors = first_location.sensors
    if not sensors:
        return {"error": "Brak sensorów dla tej lokalizacji."}

    first_sensor = sensors[0]
    first_sensor_id = first_sensor.id
    parameter_name = getattr(first_sensor.parameter, 'name', str(first_sensor.parameter))
    parameter_units = getattr(first_sensor.parameter, 'units', "")

    measurements = await fetch_measurements_for_sensor(client, first_sensor_id)
    if not measurements:
        return {"error": "Brak pomiarów dla tego sensora."}

    measurements_with_dates = [(m, parse_measurement_date(m)) for m in measurements]
    measurements_with_dates = [md for md in measurements_with_dates if md[1] is not None]

    if not measurements_with_dates:
        return {"error": "Brak poprawnych dat pomiarów."}

    latest, latest_date = sorted(measurements_with_dates, key=lambda x: x[1])[-1]
    date_str = latest_date.strftime("%d.%m.%Y %H:%M")

    parameter = getattr(latest.parameter, "name", str(latest.parameter))
    units = getattr(latest.parameter, "units", "")

    rating = None
    if latest.value is None:
        rating = "Brak danych"
    else:
        if parameter.lower() == "pm25":
            if latest.value <= 12:
                rating = "GOOD ✅"
            elif latest.value <= 35.4:
                rating = "MEDIUM ⚠️"
            else:
                rating = "BAD ❌"
        elif parameter.lower() == "co":
            co_mg_m3 = latest.value / 1000
            if co_mg_m3 <= 10:
                rating = "GOOD ✅"
            elif co_mg_m3 <= 30:
                rating = "MEDIUM ⚠️"
            else:
                rating = "BAD ❌"
        else:
            rating = None

    entry = {
        "city": city,
        "location_id": first_location.id,
        "location_name": first_location.name,
        "location_distance": round(first_location.distance or 0, 2),
        "sensor_id": first_sensor_id,
        "parameter": parameter.upper(),
        "value": latest.value,
        "units": units,
        "date": date_str,
        "rating": rating
    }

    handler[city, date_str] = entry
    handler.write_data_to_file()

    return entry

# Funkcja do zamykania klienta przy zamykaniu aplikacji
async def close_client():
    global client
    if client:
        await client.__aexit__(None, None, None)
        client = None
