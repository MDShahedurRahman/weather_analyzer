def average_temperature(records):
    if not records:
        return 0
    return sum(r["temperature"] for r in records) / len(records)


def max_temperature(records):
    if not records:
        return None
    return max(r["temperature"] for r in records)


def min_temperature(records):
    if not records:
        return None
    return min(r["temperature"] for r in records)
