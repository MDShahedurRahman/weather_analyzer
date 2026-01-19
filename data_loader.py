import csv
from config import DATA_FILE


def load_weather_data():
    records = []
    with open(DATA_FILE, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append(row)

    return records
