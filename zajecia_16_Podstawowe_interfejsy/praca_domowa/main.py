from datetime import datetime, timedelta
from weather_forecast import WeatherForecast

def interpret_rain_sum(rain_sum):
    if rain_sum is None or rain_sum < 0:
        return "Nie wiem"
    elif rain_sum == 0.0:
        return "Nie będzie padać"
    else:
        return "Będzie padać"

def main():
    weather_forecast = WeatherForecast("data.json")

    user_date = input("Podaj datę (YYYY-MM-DD). Jeśli nie podasz, zostanie użyta data jutrzejsza: ").strip()
    if not user_date:
        user_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(user_date, "%Y-%m-%d")
        except ValueError:
            print("Błędny format daty. Użyj formatu YYYY-MM-DD.")
            return

    location_name = input("Podaj nazwę lokalizacji (np. Warszawa, Poland): ").strip()
    if not location_name:
        print("Nie podano lokalizacji.")
        return

    city = location_name.split(",")[0].strip().capitalize()

    forecast = weather_forecast[(city, user_date)]
    if forecast is None:
        lat, lon = weather_forecast.get_coordinates(location_name)
        if lat is None:
            return
        rain_sum = weather_forecast.fetch_weather(lat, lon, user_date)
        forecast = interpret_rain_sum(rain_sum)
        weather_forecast[(city, user_date)] = forecast

    print(f"\n Data: {user_date}\n Lokalizacja: {city}\n Prognoza: {forecast}")

if __name__ == "__main__":
    main()
