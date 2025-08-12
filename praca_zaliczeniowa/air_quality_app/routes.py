from flask import Blueprint, render_template, request
import asyncio
from main import get_air_quality_for_city

main_page = Blueprint('main_page', __name__)
loop = asyncio.get_event_loop()

@main_page.route('/', methods=['GET', 'POST'])
def index():
    city = request.args.get("imie")
    data = error = None

    if city:
        try:
            full_data = loop.run_until_complete(get_air_quality_for_city(city))
            error = full_data.pop("error", None)
            if not error:
                daily_averages = full_data.get("daily_averages", [])
                if daily_averages:
                    last_day = daily_averages[-1]
                    data = {
                        "city": full_data["city"],
                        "location_id": full_data.get("location_id"),
                        "location_name": full_data.get("location_name"),
                        "sensor_id": full_data.get("sensor_id"),
                        "date": last_day["date"],
                        "parameter": last_day["parameter"],
                        "value": last_day["value"],
                        "rating": last_day["rating"]
                    }
                else:
                    error = "Brak danych dziennych."
        except Exception as e:
            error = str(e)

    return render_template("main_page.html", city=city, data=data, error=error)

@main_page.route('/historia')
def historia():
    from models import LocationCity
    records = LocationCity.query.order_by(LocationCity.date.desc()).all()
    entries_for_template = []
    for entry in records:
        info = {
            "location_id": entry.location_id,
            "location_name": entry.location_name,
            "sensor_id": entry.sensor_id,
            "parameter": entry.parameter,
            "value": entry.value,
            "rating": entry.rating,
        }
        entries_for_template.append((entry.city, entry.date, info))
    return render_template("historia.html", entries=entries_for_template)

@main_page.route('/pomiar')
def pomiar():
    from models import SensorMeasurement
    measurements = SensorMeasurement.query.order_by(SensorMeasurement.date.desc()).limit(100).all()
    entries = []
    for m in measurements:
        entries.append({
            "sensor_id": m.sensor_id,
            "parameter": m.parameter,
            "value": m.value,
            "date": m.date,
            "units": m.units,
        })
    return render_template("pomiar.html", entries=entries)
