import csv
from config import DATA_FILE


def load_weather_data():
    records = []
    try:
        with open(DATA_FILE, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append(row)
    except FileNotFoundError:
        pass
    return records
