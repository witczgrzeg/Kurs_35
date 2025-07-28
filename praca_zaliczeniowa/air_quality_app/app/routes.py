from flask import Blueprint, render_template, request, redirect
from .api_handler import get_latest_data
from .models import AirQuality
from . import db

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        return redirect(f"/results?city={city}")
    return render_template("index.html")

@main.route("/results")
def results():
    city = request.args.get("city")
    data = get_latest_data(city)
    results = []

    for result in data["results"]:
        for m in result["measurements"]:
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
