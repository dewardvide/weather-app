import requests

from .model import GeoCodingError, WeatherData, WeatherDataError


class WeatherClient:
    def __init__(self, city: str):
        self.city = city

    def get_coordinates(self) -> tuple[float, float]:

        geo_coding_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_coding_parameters = {"name": self.city}
        response = requests.get(geo_coding_url, params=geo_coding_parameters)
        city_data = response.json()

        if response.status_code != 200 or not city_data.get("results"):
            raise GeoCodingError(
                f"Failed to get coordinates for {self.city}: {response.status_code}"
            )

        first_result = city_data["results"][0]
        latitude = first_result["latitude"]
        longitude = first_result["longitude"]

        return latitude, longitude

    def get_weather_data(self) -> WeatherData:
        latitude, longitude = self.get_coordinates()
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_parameters: dict[str, str | float | int] = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
            ),
            "forecast_days": 1,
        }
        response = requests.get(weather_url, params=weather_parameters)

        if response.status_code != 200:
            raise WeatherDataError(
                f"Failed to get weather data for {self.city}: {response.status_code}"
            )

        json_response = response.json()
        weather_data = WeatherData.from_api_response(json_response, self.city)
        return weather_data
