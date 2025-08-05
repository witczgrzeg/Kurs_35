from flask import Blueprint, render_template, request
import asyncio
from main import get_air_quality_for_city
from file_handler import FileHandler

main_page = Blueprint('main_page', __name__)
loop = asyncio.get_event_loop()
DATA_FILE = "data.json"

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
    entries = list(FileHandler(DATA_FILE).items())
    return render_template("historia.html", entries=entries)
