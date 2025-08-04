from flask import Blueprint, render_template, request
import asyncio
from main import get_air_quality_for_city
from file_handler import FileHandler

DATA_FILE = "data.json"

main_page = Blueprint('main_page', __name__)

# Utwórz globalną pętlę i klienta asynchronicznego
event_loop = asyncio.get_event_loop()

@main_page.route('/', methods=['GET'])
def index():
    city = request.args.get('imie')
    data = None
    error = None

    if city:
        try:
            # Uruchamiamy asynchroniczną funkcję w istniejącej pętli
            data = event_loop.run_until_complete(get_air_quality_for_city(city))
            if "error" in data:
                error = data["error"]
                data = None
        except Exception as e:
            error = str(e)

    return render_template("main_page.html", city=city, data=data, error=error)

@main_page.route('/historia')
def historia():
    handler = FileHandler(DATA_FILE)
    entries = list(handler.items())
    return render_template("historia.html", entries=entries)
