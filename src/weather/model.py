from dataclasses import dataclass

weathercodes = {0: "Clear sky",
                   1: "Mainly clear",
                   2: "Partly cloudy",
                   3: "Overcast",
                   45: "Fog",
                   48: "Depositng rime fog",
                   51: "Drizzle: Light",
                   53: "Drizzle: Moderate",
                   55: "Drizzle: Heavy",
                   56: "Freezing Drizzle: Light",
                   57: "Freezing Drizzle: Heavy", 
                   61: "Rain: Slight",
                   63: "Rain: Moderate",
                   65: "Rain: Heavy intensity",
                   66: "Freezing Rain: Light intensity",
                   67: "Freezing Rain: Heavy intensity",
                   71: "Snow fall: Slight intensity",
                   73: "Snow fall: Moderate intensity",
                   75: "Snow fall: Heavy intensity",
                   77: "Snow grains",
                   80: "Rain showers: Slight",
                   81: "Rain showers: Moderate",
                   82: "Rain showers: Violent",
                   85: "Snow showers slight",
                   86: "Snow showers heavy",
                   95: "Thunderstorm: Slight or moderate",
                   96: "Thunderstorm with slight hail",
                   99: "Thunderstorm with heavy hail"}

@dataclass
class WeatherData:
    city: str
    temperature: float
    humidity: int
    wind_speed: float
    description: str

    @classmethod
    def from_api_response(cls, API_response: dict, city: str):
        current_weather = API_response.get("current", {})
        temperature = current_weather.get("temperature_2m", 0.0)
        humidity = current_weather.get("relative_humidity_2m", 0)
        wind_speed = current_weather.get("wind_speed_10m", 0.0)
        weathercode = current_weather.get("weathercode", 0)
        description = weathercodes.get(weathercode, "Unknown weather code")

        return cls(city=city, temperature=temperature, humidity=humidity, wind_speed=wind_speed, description=description)