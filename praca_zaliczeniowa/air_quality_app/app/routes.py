from flask import Blueprint, render_template, request, redirect
from .api_handler import geocode_city, get_latest_data_by_coords
from .models import AirQuality
from . import db

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        return redirect(f"/results?city={city}")
    return render_template("index.html")  # bez cities

@main.route("/results")
def results():
    city = request.args.get("city")
    if not city:
        return "Proszę podać miasto lub region.", 400

    lat, lon = geocode_city(city)
    if lat is None or lon is None:
        return f"Nie udało się znaleźć współrzędnych dla '{city}'.", 404

    data = get_latest_data_by_coords(lat, lon)

    if "error" in data:
        return data["error"], 404

    if "results" not in data or not data["results"]:
        return f"Brak danych dla miasta/regionu: {city}", 404

    results = []
    for result in data["results"]:
        for m in result.get("measurements", []):
            aq = AirQuality(
                city=city,
                parameter=m["parameter"],
                value=m["value"],
                unit=m["unit"],
                date_utc=m["lastUpdated"]
            )
            db.session.add(aq)
            results.append(aq)

    db.session.commit()
    return render_template("result.html", city=city, results=results)
