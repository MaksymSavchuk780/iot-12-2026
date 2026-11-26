"""Weather records and calendar management."""

from enum import Enum


class WeatherType(Enum):
    """Supported weather conditions."""

    SUNNY = "SUNNY"
    CLOUDY = "CLOUDY"
    RAINY = "RAINY"
    FOGGY = "FOGGY"
    SNOWY = "SNOWY"


def _validate_instance(value, expected_type, name):
    """Validate that value is an instance of expected_type."""
    if not isinstance(value, expected_type):
        raise TypeError(
            f"{name} must be a {expected_type.__name__}, "
            f"got {type(value).__name__}"
        )


class Weather:
    """Single-day weather record."""

    def __init__(
        self,
        day,
        city,
        country,
        temp,
        humidity,
        wind_speed,
        weather_type
    ):
        """Initialize a single-day weather record."""
        _validate_instance(weather_type, WeatherType, "weather_type")
        self._day = day
        self._city = city
        self._country = country
        self._temp = temp
        self._humidity = humidity
        self._wind_speed = wind_speed
        self._weather_type = weather_type

    def __del__(self):
        """Print a deletion notice when the record is finalized."""
        if not (
            hasattr(self, "_city")
            and hasattr(self, "_day")
            and hasattr(self, "_weather_type")
        ):
            return
        print(
            f"[Деструктор] Видалено запис погоди: "
            f"{self._city} (день {self._day})"
        )

    def __str__(self):
        """Return a formatted summary of the weather record."""
        return (
            f"День: {self._day} | {self._city}, {self._country} | "
            f"Температура: {self._temp}°C | "
            f"Вологість: {self._humidity}% | "
            f"Вітер: {self._wind_speed} м/с | "
            f"Стан: {self._weather_type.value}"
        )

    @property
    def day(self):
        """Day of the month."""
        return self._day

    @day.setter
    def day(self, value):
        self._day = value

    @property
    def city(self):
        """City name."""
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def country(self):
        """Country name."""
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def temp(self):
        """Air temperature in degrees Celsius."""
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = value

    @property
    def humidity(self):
        """Relative air humidity in percent."""
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        self._humidity = value

    @property
    def wind_speed(self):
        """Wind speed in meters per second."""
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value):
        self._wind_speed = value

    @property
    def weather_type(self):
        """WeatherType condition (raises TypeError on bad value)."""
        return self._weather_type

    @weather_type.setter
    def weather_type(self, value):
        _validate_instance(value, WeatherType, "weather_type")
        self._weather_type = value

    @staticmethod
    def is_lviv_weather(humidity, weather_type):
        """Predict Lviv-like weather and print the result."""
        _validate_instance(weather_type, WeatherType, "weather_type")
        is_typical = humidity > 80 and weather_type == WeatherType.RAINY
        if is_typical:
            print("The typical day in Lviv")
        else:
            print("You're lucky, man")
        return is_typical


class WeatherCalendar:
    """Container for managing and sorting Weather records."""

    def __init__(self, records=None):
        """Initialize the calendar from optional Weather records."""
        if records is None:
            self.records = []
            return
        record_list = list(records)
        for record in record_list:
            _validate_instance(record, Weather, "record")
        self.records = record_list

    def __del__(self):
        """Print a deletion notice when the calendar is finalized."""
        if not hasattr(self, "records"):
            return
        print(
            f"[Деструктор] Видалено WeatherCalendar "
            f"із {len(self.records)} записами."
        )

    def add_weather(self, weather):
        """Validate and append a Weather record to the calendar."""
        _validate_instance(weather, Weather, "weather")
        self.records.append(weather)

    def sort_by_day(self):
        """Sort stored records in place by day in ascending order."""
        self.records.sort(key=lambda weather: weather.day)

    def display(self):
        """Print all records, or a notice if the calendar is empty."""
        if not self.records:
            print("Календар порожній.")
        else:
            for weather in self.records:
                print(weather)


def find_max_temperature(weather_list, day):
    """Find and print the highest temperature for a given day."""
    matching = [
        weather.temp
        for weather in weather_list
        if weather.day == day
    ]

    if not matching:
        print("Not enough data")
        return None

    max_temp = max(matching)
    print(f"Максимальна температура за день {day}: {max_temp}°C")
    return max_temp


def main():
    """Demonstrate Weather, WeatherCalendar, and predictions."""
    lviv_weather = Weather(
        day=15,
        city="Lviv",
        country="Ukraine",
        temp=11.5,
        humidity=89.0,
        wind_speed=4.2,
        weather_type=WeatherType.RAINY
    )
    kyiv_weather = Weather(
        day=3,
        city="Kyiv",
        country="Ukraine",
        temp=18.0,
        humidity=55.0,
        wind_speed=3.0,
        weather_type=WeatherType.SUNNY
    )
    odesa_weather = Weather(
        day=10,
        city="Odesa",
        country="Ukraine",
        temp=21.4,
        humidity=60.0,
        wind_speed=6.1,
        weather_type=WeatherType.CLOUDY
    )
    kharkiv_weather = Weather(
        day=10,
        city="Kharkiv",
        country="Ukraine",
        temp=24.2,
        humidity=45.0,
        wind_speed=2.5,
        weather_type=WeatherType.SUNNY
    )
    dnipro_weather = Weather(
        day=25,
        city="Dnipro",
        country="Ukraine",
        temp=30.0,
        humidity=70.0,
        wind_speed=5.0,
        weather_type=WeatherType.SUNNY
    )

    calendar = WeatherCalendar([
        lviv_weather, kyiv_weather, odesa_weather,
        kharkiv_weather, dnipro_weather
    ])

    print("--- Записи погоди ---")
    calendar.display()

    print("\n--- Сортування записів за днем ---")
    calendar.sort_by_day()
    calendar.display()

    print("\n--- Пошук максимальної температури ---")
    find_max_temperature(calendar.records, 10)
    find_max_temperature(calendar.records, 25)

    print("\n--- Перевірка на погоду у Львові (is_lviv_weather) ---")
    Weather.is_lviv_weather(lviv_weather.humidity, lviv_weather.weather_type)
    Weather.is_lviv_weather(kyiv_weather.humidity, kyiv_weather.weather_type)
    Weather.is_lviv_weather(dnipro_weather.humidity, dnipro_weather.weather_type)
    Weather.is_lviv_weather(85, WeatherType.RAINY)

    print("\n--- Демонстрація функцій доступу (getters / setters) ---")
    print(
        f"Початкова температура в "
        f"{kyiv_weather.city}: {kyiv_weather.temp}°C"
    )
    kyiv_weather.temp = 19.5
    print(
        f"Змінена температура в "
        f"{kyiv_weather.city}: {kyiv_weather.temp}°C"
    )

    print("\n--- Видалення об'єктів (деструктори) ---")
    del calendar
    del lviv_weather, kyiv_weather, odesa_weather
    del kharkiv_weather, dnipro_weather


if __name__ == "__main__":
    main()
