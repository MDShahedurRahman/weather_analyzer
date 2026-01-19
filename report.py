from analyzer import average_temperature, max_temperature, min_temperature


def summary_report(records):
    return {
        "average_temp": average_temperature(records),
        "max_temp": max_temperature(records),
        "min_temp": min_temperature(records),
        "total_records": len(records)
    }
