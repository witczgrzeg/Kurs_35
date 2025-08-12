from datetime import datetime
from openaq import AsyncOpenAQ
from classification import classify_air_quality
from geopy.geocoders import Nominatim

API_KEY = "9842cf2ba34018b9ff7e2f1593819e26e814a4f71f0001e65bf688f92e25c865"
client: AsyncOpenAQ = None

def get_coordinates(city: str):
    geolocator = Nominatim(user_agent="moja_aplikacja")
    loc = geolocator.geocode(city)
    if not loc:
        raise ValueError(f"Nie znaleziono współrzędnych: {city}")
    return loc.latitude, loc.longitude

async def get_air_quality_for_city(city: str):
    from models import db, LocationCity, SensorMeasurement

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

    measurements = await client.measurements.list(sensors_id=sensor.id, data="days", limit=10)
    results = measurements.results

    if not results:
        return {"error": "Brak pomiarów."}

    daily_averages = []
    now_str = datetime.now().strftime("%d.%m.%Y %H:%M")

    for r in results:
        value = getattr(r, "value", None)
        param_obj = getattr(r, "parameter", None)
        unit = getattr(r, "unit", None)

        if value is None or param_obj is None:
            continue

        if hasattr(param_obj, "name"):
            param = param_obj.name.upper()
        else:
            param = str(param_obj).upper()

        rating = classify_air_quality(param.lower(), value)

        record = LocationCity.query.filter_by(city=city, date=now_str, parameter=param).first()
        if not record:
            record = LocationCity()

        record.city = city
        record.location_id = str(loc.id) if hasattr(loc, 'id') else None
        record.location_name = loc.name
        record.sensor_id = sensor.id
        record.parameter = param
        record.value = str(value)
        record.date = now_str
        record.rating = rating

        db.session.add(record)

        measurement = SensorMeasurement(
            sensor_id=sensor.id,
            parameter=param,
            value=str(value),
            date=now_str,
            units=unit
        )
        db.session.add(measurement)

        daily_averages.append({
            "date": now_str,
            "value": value,
            "parameter": param,
            "rating": rating,
        })

    db.session.commit()

    return {
        "city": city,
        "location_id": str(loc.id) if hasattr(loc, 'id') else None,
        "location_name": loc.name,
        "sensor_id": sensor.id,
        "daily_averages": daily_averages
    }


async def close_client():
    global client
    if client:
        await client.__aexit__(None, None, None)
        client = None
