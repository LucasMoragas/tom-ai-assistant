from pydantic import BaseModel

class UserMessage(BaseModel):
    message: str

class WeatherData(BaseModel):
    temperature: float
    humidity: float
    precipitation: float
    wind_speed: float

class WeatherForecast(BaseModel):
    day: str
    temperature: float
    precipitation: float

class WeatherResponse(BaseModel):
    current_weather: WeatherData
    forecast: list[WeatherForecast]

class ChatResponse(BaseModel):
    response: str 