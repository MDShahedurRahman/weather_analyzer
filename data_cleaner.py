from utils import validate_date, validate_number


def clean_weather_data(raw_records):
    cleaned = []
    for r in raw_records:
        if (
            validate_date(r["date"])
        ):
            cleaned.append({
                "date": r["date"],
                "city": r["city"]
            })
    return cleaned
