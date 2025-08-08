from datetime import datetime
from geopy.geocoders import Nominatim
from openaq import AsyncOpenAQ
from classification import classify_air_quality

API_KEY = "9842cf2ba34018b9ff7e2f1593819e26e814a4f71f0001e65bf688f92e25c865"
client: AsyncOpenAQ = None

def get_coordinates(city):
    loc = Nominatim(user_agent="moja_aplikacja").geocode(city)
    if not loc:
        raise ValueError(f"Nie znaleziono współrzędnych: {city}")
    return loc.latitude, loc.longitude

async def get_air_quality_for_city(city):
    from models import db, LocationCity

    global client
    if not client:
        client = AsyncOpenAQ(api_key=API_KEY)
        await client.__aenter__()

    lat, lon = get_coordinates(city)

    locations = await client.locations.list(coordinates=[lat, lon], radius=10000, limit=10)
    if not locations.results:
        return {"error": "Brak lokalizacji."}

    loc = sorted(locations.results, key=lambda x: x.distance or float('inf'))[0]
    sensors = loc.sensors
    if not sensors:
        return {"error": "Brak sensorów."}

    sensor = sensors[0]
    measurements = await client.measurements.list(sensors_id=sensor.id, limit=100)
    results = measurements.results

    if not results:
        return {"error": "Brak pomiarów."}

    valid = [
        (m, datetime.fromisoformat(m.period.datetime_from.local))
        for m in results if hasattr(m.period, "datetime_from")
    ]
    if not valid:
        return {"error": "Brak dat."}

    latest, dt = sorted(valid, key=lambda x: x[1])[-1]
    date_str = dt.strftime("%d.%m.%Y %H:%M")

    value = latest.value or 0
    param = getattr(latest.parameter, "name", str(latest.parameter)).lower()
    units = getattr(latest.parameter, "units", "")

    rating = classify_air_quality(param, value)

    record = LocationCity.query.filter_by(city=city, date=date_str).first()
    if not record:
        record = LocationCity()

    record.city = city
    record.location_id = str(loc.id) if hasattr(loc, 'id') else None
    record.location_distance = float(loc.distance) if hasattr(loc, 'distance') else None
    record.location_name = loc.name
    record.sensor_id = sensor.id
    record.parameter = param.upper()
    record.value = str(value)
    record.units = units
    record.date = date_str
    record.rating = rating

    db.session.add(record)
    db.session.commit()

    return {
        "city": record.city,
        "location_id": record.location_id,
        "location_distance": record.location_distance,
        "location_name": record.location_name,
        "sensor_id": record.sensor_id,
        "parameter": record.parameter,
        "value": record.value,
        "units": record.units,
        "date": record.date,
        "rating": record.rating
    }

async def close_client():
    global client
    if client:
        await client.__aexit__(None, None, None)
        client = None
