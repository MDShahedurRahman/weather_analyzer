from utils import validate_date, validate_number


def clean_weather_data(raw_records):
    cleaned = []
    for r in raw_records:
        if (
            validate_date(r["date"])
            and validate_number(r["temperature"])
        ):
            cleaned.append({
                "date": r["date"],
                "city": r["city"],
                "temperature": float(r["temperature"])
            })
    return cleaned
