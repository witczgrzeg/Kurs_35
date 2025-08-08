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
            data = loop.run_until_complete(get_air_quality_for_city(city))
            error = data.pop("error", None)
        except Exception as e:
            error = str(e)

    return render_template("main_page.html", city=city, data=data, error=error)

@main_page.route('/historia')
def historia():
    from models import LocationCity
    records = LocationCity.query.order_by(LocationCity.date.desc()).all()
    print(f"Liczba rekordów w bazie: {len(records)}")
    entries_for_template = []
    for entry in records:
        info = {
            "location_id": entry.location_id,
            "location_distance": entry.location_distance,
            "location_name": entry.location_name,
            "sensor_id": entry.sensor_id,
            "parameter": entry.parameter,
            "value": entry.value,
            "units": entry.units,
            "rating": entry.rating,
        }
        entries_for_template.append((entry.city, entry.date, info))

    return render_template("historia.html", entries=entries_for_template)

