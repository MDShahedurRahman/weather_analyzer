from data_loader import load_weather_data
from data_cleaner import clean_weather_data
from analyzer import filter_by_city
from report import summary_report, print_report


def main():
    raw = load_weather_data()
    cleaned = clean_weather_data(raw)
    city_data = filter_by_city(cleaned, "New York")
    report = summary_report(city_data)


if __name__ == "__main__":
    main()
