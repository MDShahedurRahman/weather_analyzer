from analyzer import average_temperature, max_temperature, min_temperature


def summary_report(records):
    return {
        "average_temp": average_temperature(records),
        "max_temp": max_temperature(records),
        "min_temp": min_temperature(records),
        "total_records": len(records)
    }


def print_report(report):
    print("Weather Summary Report")
    print("----------------------")
    print(f"Average Temp: {report['average_temp']}")
    print(f"Max Temp: {report['max_temp']}")
    print(f"Min Temp: {report['min_temp']}")
    print(f"Records: {report['total_records']}")
