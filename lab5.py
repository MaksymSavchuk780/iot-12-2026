"""Module for working with weather records and a weather calendar."""

from enum import Enum


class WeatherType(Enum):
    """Enumeration of possible weather types."""

    SUNNY = "SUNNY"
    CLOUDY = "CLOUDY"
    RAINY = "RAINY"
    FOGGY = "FOGGY"
    SNOWY = "SNOWY"


def _validate_instance(value, expected_type, name):
    """Ensure value is an instance of expected_type."""
    if not isinstance(value, expected_type):
        raise TypeError(
            f"{name} must be a {expected_type.__name__}, "
            f"got {type(value).__name__}"
        )


class Weather:
    """Stores and processes a single-day weather record."""

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
        """Initialize a weather record.

        Args:
            day: Day of the month.
            city: City name.
            country: Country name.
            temp: Air temperature (°C).
            humidity: Air humidity (%).
            wind_speed: Wind speed (m/s).
            weather_type: Weather condition (WeatherType).

        Raises:
            TypeError: If weather_type is not a WeatherType instance.
        """
        _validate_instance(weather_type, WeatherType, "weather_type")
        self._day = day
        self._city = city
        self._country = country
        self._temp = temp
        self._humidity = humidity
        self._wind_speed = wind_speed
        self._weather_type = weather_type

    def __del__(self):
        """Print a message when the weather record is deleted."""
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
        """Return a human-readable string representation of the record."""
        return (
            f"День: {self._day} | {self._city}, {self._country} | "
            f"Температура: {self._temp}°C | "
            f"Вологість: {self._humidity}% | "
            f"Вітер: {self._wind_speed} м/с | "
            f"Стан: {self._weather_type.value}"
        )

    @property
    def day(self):
        """Return the day of the month."""
        return self._day

    @day.setter
    def day(self, value):
        """Set the day of the month."""
        self._day = value

    @property
    def city(self):
        """Return the city name."""
        return self._city

    @city.setter
    def city(self, value):
        """Set the city name."""
        self._city = value

    @property
    def country(self):
        """Return the country name."""
        return self._country

    @country.setter
    def country(self, value):
        """Set the country name."""
        self._country = value

    @property
    def temp(self):
        """Return the temperature."""
        return self._temp

    @temp.setter
    def temp(self, value):
        """Set the temperature."""
        self._temp = value

    @property
    def humidity(self):
        """Return the humidity."""
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        """Set the humidity."""
        self._humidity = value

    @property
    def wind_speed(self):
        """Return the wind speed."""
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value):
        """Set the wind speed."""
        self._wind_speed = value

    @property
    def weather_type(self):
        """Return the weather type."""
        return self._weather_type

    @weather_type.setter
    def weather_type(self, value):
        """Set the weather type.

        Raises:
            TypeError: If value is not a WeatherType instance.
        """
        _validate_instance(value, WeatherType, "weather_type")
        self._weather_type = value

    def is_lviv_weather(self):
        """Check whether this record represents typical Lviv weather.

        Returns:
            bool: True for Lviv with humidity over 80% and RAINY weather.
        """
        return (
            self._city == "Lviv"
            and self._humidity > 80
            and self._weather_type == WeatherType.RAINY
        )

    @staticmethod
    def check_lviv_conditions(humidity, weather_type):
        """Check whether the given conditions match typical Lviv weather.

        Args:
            humidity: Air humidity (%).
            weather_type: Weather condition (WeatherType).

        Returns:
            bool: True if humidity exceeds 80% and weather type is RAINY.

        Raises:
            TypeError: If weather_type is not a WeatherType instance.
        """
        _validate_instance(weather_type, WeatherType, "weather_type")
        return humidity > 80 and weather_type == WeatherType.RAINY


class WeatherCalendar:
    """Container for a collection of weather records."""

    def __init__(self, records=None):
        """Initialize the weather calendar.

        Args:
            records: Optional iterable of Weather objects.

        Raises:
            TypeError: If records is not iterable or contains non-Weather
                items.
        """
        if records is None:
            self.records = []
            return
        record_list = list(records)
        for record in record_list:
            _validate_instance(record, Weather, "record")
        self.records = record_list

    def __del__(self):
        """Print a message when the weather calendar is deleted."""
        if not hasattr(self, "records"):
            return
        print(
            f"[Деструктор] Видалено WeatherCalendar "
            f"із {len(self.records)} записами."
        )

    def add_weather(self, weather):
        """Add a weather record to the calendar.

        Args:
            weather: Weather object to add.

        Raises:
            TypeError: If weather is not a Weather instance.
        """
        _validate_instance(weather, Weather, "weather")
        self.records.append(weather)

    def sort_by_day(self):
        """Sort records by day number in ascending order."""
        self.records.sort(key=lambda weather: weather.day)

    def display(self):
        """Print all records or a message if the calendar is empty."""
        if not self.records:
            print("Календар порожній.")
        else:
            for weather in self.records:
                print(weather)


def find_max_temperature(weather_list, day):
    """Find the maximum temperature for a given day.

    Args:
        weather_list: List of Weather objects.
        day: Day number to search for.

    Returns:
        float or None: The maximum temperature, or None
        if no records exist for the given day.
    """
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
    """Demonstrate the Weather and WeatherCalendar classes."""
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
    print(lviv_weather.is_lviv_weather())
    print(kyiv_weather.is_lviv_weather())
    print(dnipro_weather.is_lviv_weather())
    print(Weather.check_lviv_conditions(85, WeatherType.RAINY))

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
