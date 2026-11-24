from enum import Enum


class WeatherType(Enum):
    SUNNY = "SUNNY"
    CLOUDY = "CLOUDY"
    RAINY = "RAINY"
    FOGGY = "FOGGY"
    SNOWY = "SNOWY"


class Weather:
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
        if not isinstance(weather_type, WeatherType):
            raise TypeError(f"weather_type must be a WeatherType, got {type(weather_type).__name__}")
        self._day = day
        self._city = city
        self._country = country
        self._temp = temp
        self._humidity = humidity
        self._wind_speed = wind_speed
        self._weather_type = weather_type

    def __del__(self):
        print(f"[Деструктор] Видалено запис погоди: {self._city} (день {self._day})")

    def __str__(self):
        return (
            f"День: {self._day} | {self._city}, {self._country} | "
            f"Температура: {self._temp}°C | Вологість: {self._humidity}% | "
            f"Вітер: {self._wind_speed} м/с | Стан: {self._weather_type.value}"
        )

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = value

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        self._humidity = value

    @property
    def wind_speed(self):
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value):
        self._wind_speed = value

    @property
    def weather_type(self):
        return self._weather_type

    @weather_type.setter
    def weather_type(self, value):
        if not isinstance(value, WeatherType):
            raise TypeError(f"weather_type must be a WeatherType, got {type(value).__name__}")
        self._weather_type = value

    def is_lviv_weather(self, humidity=None, weather_type=None):
        if isinstance(self, Weather):
            if humidity is None:
                humidity = self._humidity
            if weather_type is None:
                weather_type = self._weather_type
        else:
            weather_type = humidity
            humidity = self

        if isinstance(weather_type, WeatherType):
            weather_val = weather_type.value
        else:
            weather_val = str(weather_type)

        if humidity > 80 and weather_val == "RAINY":
            return True
        return False


class WeatherCalendar:
    def __init__(self, records=None):
        self.records = list(records) if records is not None else []

    def __del__(self):
        print(f"[Деструктор] Видалено WeatherCalendar із {len(self.records)} записами.")

    def add_weather(self, weather):
        self.records.append(weather)

    def sort_by_day(self):
        self.records.sort(key=lambda weather: weather.day)

    def display(self):
        if not self.records:
            print("Календар порожній.")
        else:
            for weather in self.records:
                print(weather)


def find_max_temperature(weather_list, day):
    matching = [weather.temp for weather in weather_list if weather.day == day]

    if not matching:
        print("Not enough data")
        return None

    max_temp = max(matching)
    print(f"Максимальна температура за день {day}: {max_temp}°C")
    return max_temp


def main():
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

    calendar = WeatherCalendar([lviv_weather, kyiv_weather, odesa_weather, kharkiv_weather, dnipro_weather])

    print("--- Записи погоди ---")
    calendar.display()

    print("\n--- Сортування записів за днем ---")
    calendar.sort_by_day()
    calendar.display()

    print("\n--- Пошук максимальної температури (find_max_temperature) ---")
    find_max_temperature(calendar.records, 10)
    find_max_temperature(calendar.records, 25)

    print("\n--- Перевірка на погоду у Львові (is_lviv_weather) ---")
    print(lviv_weather.is_lviv_weather())
    print(kyiv_weather.is_lviv_weather())
    print(dnipro_weather.is_lviv_weather())
    Weather.is_lviv_weather(85, WeatherType.RAINY)

    print("\n--- Демонстрація функцій доступу (getters / setters) ---")
    print(f"Початкова температура в {kyiv_weather.city}: {kyiv_weather.temp}°C")
    kyiv_weather.temp = 19.5
    print(f"Змінена температура в {kyiv_weather.city}: {kyiv_weather.temp}°C")

    print("\n--- Видалення об'єктів (деструктори) ---")
    del calendar
    del lviv_weather, kyiv_weather, odesa_weather, kharkiv_weather, dnipro_weather


if __name__ == "__main__":
    main()
