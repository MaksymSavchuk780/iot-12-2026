from enum import Enum


class WeatherType(Enum):
    SUNNY = "SUNNY"
    CLOUDY = "CLOUDY"
    RAINY = "RAINY"
    FOGGY = "FOGGY"
    SNOWY = "SNOWY"


class Weather:
    def __init__(self, day, city, country, temp, humidity, wind_speed, weather_type):
        self._day = day
        self._city = city
        self._country = country
        self._temp = temp
        self._humidity = humidity
        self._wind_speed = wind_speed
        self._weather_type = weather_type

    def __del__(self):
        print(f"[Деструктор] Видалено запис погоди: {self._city} (день {self._day})")

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
        self._weather_type = value

    def display(self):
        print(
            f"День: {self._day} | {self._city}, {self._country} | "
            f"Температура: {self._temp}°C | Вологість: {self._humidity}% | "
            f"Вітер: {self._wind_speed} м/с | Стан: {self._weather_type.value}"
        )

    def isLvivWeather(self, humidity=None, weather_type=None):
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
            print("The typical day in Lviv")
        else:
            print("You’re lucky, man")


class WeatherCalendar:
    def __init__(self, records=None):
        if records is None:
            self.records = []
        else:
            self.records = records

    def __del__(self):
        print(f"[Деструктор] Видалено WeatherCalendar із {len(self.records)} записами.")

    def add_weather(self, weather):
        self.records.append(weather)

    def sort_by_day(self):
        self.records.sort(key=lambda w: w.day)

    def display(self):
        if len(self.records) == 0:
            print("Календар порожній.")
        else:
            for w in self.records:
                w.display()


def findMaxTemprature(weather_list, day):
    matching = []
    for w in weather_list:
        if w.day == day:
            matching.append(w.temp)

    if len(matching) == 0:
        print("Not enough data")
        return None

    max_temp = max(matching)
    print(f"Максимальна температура за день {day}: {max_temp}°C")
    return max_temp


def main():
    w1 = Weather(15, "Lviv", "Ukraine", 11.5, 89.0, 4.2, WeatherType.RAINY)
    w2 = Weather(3, "Kyiv", "Ukraine", 18.0, 55.0, 3.0, WeatherType.SUNNY)
    w3 = Weather(10, "Odesa", "Ukraine", 21.4, 60.0, 6.1, WeatherType.CLOUDY)
    w4 = Weather(10, "Kharkiv", "Ukraine", 24.2, 45.0, 2.5, WeatherType.SUNNY)
    w5 = Weather(25, "Dnipro", "Ukraine", 30.0, 70.0, 5.0, WeatherType.SUNNY)

    calendar = WeatherCalendar([w1, w2, w3, w4, w5])

    print("--- Записи погоди ---")
    calendar.display()

    print("\n--- Сортування записів за днем ---")
    calendar.sort_by_day()
    calendar.display()

    print("\n--- Пошук максимальної температури (findMaxTemprature) ---")
    findMaxTemprature(calendar.records, 10)
    findMaxTemprature(calendar.records, 25)

    print("\n--- Перевірка на погоду у Львові (isLvivWeather) ---")
    w1.isLvivWeather()
    w2.isLvivWeather()
    w5.isLvivWeather()
    Weather.isLvivWeather(85, WeatherType.RAINY)

    print("\n--- Демонстрація функцій доступу (getters / setters) ---")
    print(f"Початкова температура в {w2.city}: {w2.temp}°C")
    w2.temp = 19.5
    print(f"Змінена температура в {w2.city}: {w2.temp}°C")

    print("\n--- Видалення об'єктів (деструктори) ---")
    del calendar
    del w1, w2, w3, w4


if __name__ == "__main__":
    main()
