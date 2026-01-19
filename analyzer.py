def average_temperature(records):
    if not records:
        return 0
    return sum(r["temperature"] for r in records) / len(records)
