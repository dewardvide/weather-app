from .model import WeatherData


def display(weather_data: WeatherData) -> str:
    return f"""
    ==========It is currently {weather_data.description} in {WeatherData.city}==========
        Current Temperature : {weather_data.temperature}
        Current Humidity : {weather_data.humidity}
        Current Windspeed : {weather_data.wind_speed}
    """
