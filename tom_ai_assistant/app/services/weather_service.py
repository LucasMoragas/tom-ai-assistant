from ..models.schemas import WeatherResponse, WeatherData, WeatherForecast

class WeatherService:
    @staticmethod
    def get_weather_data() -> WeatherResponse:
        """Get mock weather data for testing purposes"""
        return WeatherResponse(
            current_weather=WeatherData(
                temperature=21,
                humidity=85,
                precipitation=7,
                wind_speed=15
            ),
            forecast=[
                WeatherForecast(day="Saturday", temperature=24, precipitation=2),
                WeatherForecast(day="Sunday", temperature=24, precipitation=0.2),
                WeatherForecast(day="Monday", temperature=23, precipitation=0.5)
            ]
        ) 