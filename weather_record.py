class WeatherRecord:
    def __init__(self, date, city, temperature, humidity):
        self.date = date
        self.city = city
        self.temperature = temperature
        self.humidity = humidity

    def to_dict(self):
        return {
            "date": self.date,
            "city": self.city,
            "temperature": self.temperature,
            "humidity": self.humidity
        }
