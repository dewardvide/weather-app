from dataclasses import dataclass
from typing import Any


class WeatherDataError(Exception):
    """Custom exception for errors in WeatherData processing."""

    pass


weathercodes = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
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
    99: "Thunderstorm with heavy hail",
}


@dataclass
class WeatherData:
    city: str
    temperature: float
    humidity: int
    wind_speed: float
    description: str

    @staticmethod
    def validate_api_response(api_response: dict[str, Any]) -> None:
        """Validate the API response for required fields."""

        if not api_response:
            raise WeatherDataError("API response is empty or invalid")

        current_weather = api_response.get("current")
        if not current_weather:
            raise WeatherDataError(
                "Current weather data is missing in the API response"
            )

        required_fields = [
            "temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m",
            "weathercode",
        ]
        for field in required_fields:
            if field not in current_weather:
                raise WeatherDataError(f"{field} data is missing in the API response")

    @classmethod
    def from_api_response(
        cls, api_response: dict[str, Any], city: str
    ) -> "WeatherData":

        cls.validate_api_response(api_response)
        current_weather: dict[str, Any] = {}

        current_weather = api_response["current"]
        temperature = current_weather["temperature_2m"]
        humidity = current_weather["relative_humidity_2m"]
        wind_speed = current_weather["wind_speed_10m"]
        weathercode = current_weather["weathercode"]
        description = weathercodes[weathercode]

        return cls(
            city=city,
            temperature=temperature,
            humidity=humidity,
            wind_speed=wind_speed,
            description=description,
        )
