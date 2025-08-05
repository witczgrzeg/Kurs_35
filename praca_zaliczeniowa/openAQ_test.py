from openaq import OpenAQ
import csv

# Twój klucz API
API_KEY = "9842cf2ba34018b9ff7e2f1593819e26e814a4f71f0001e65bf688f92e25c865"

# Inicjalizacja klienta
client = OpenAQ(api_key=API_KEY)

# Pobranie najnowszych pomiarów dla parametru o ID = 2
response = client.parameters.latest(parameters_id=35248, limit=1000)

# Zamknięcie klienta
client.close()

# Wyniki to lista obiektów ParameterLatest
results = response.results

# Zapis do CSV
with open("latest_parameters.csv", mode="w", newline="", encoding="utf-8") as csvfile:
    fieldnames = [
        "location", "city", "country",
        "parameter", "value", "unit",
        "datetime_utc"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for item in results:
        writer.writerow({
            "location": item.location,
            "city": item.city,
            "country": item.country,
            "parameter": item.parameter,
            "value": item.value,
            "unit": item.unit,
            "datetime_utc": item.date.utc
        })

print("✅ Dane zapisane do latest_parameters.csv")
