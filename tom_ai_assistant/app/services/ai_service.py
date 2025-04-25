from openai import OpenAI
from app.models.schemas import WeatherResponse, ChatResponse
from app.config.config import get_settings

class AIService:
    def __init__(self):
        settings = get_settings()
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = "gpt-4.1-nano-2025-04-14"

    def generate_response(self, user_message: str, weather_data: WeatherResponse) -> ChatResponse:
        """Generate a response using OpenAI's model with weather context"""
        context = self._create_context(weather_data)
        full_prompt = f"{context}\n\nUser question: {user_message}"
        
        response = self.client.responses.create(
            model=self.model,
            input=full_prompt
        )
        
        return ChatResponse(response=response.output_text)

    def _create_context(self, weather_data: WeatherResponse) -> str:
        """Create the context for the AI including weather information"""
        return f"""You are a cherry tomato cultivation expert. 
        Current weather conditions: Temperature: {weather_data.current_weather.temperature}°C, 
        Humidity: {weather_data.current_weather.humidity}%, 
        Precipitation: {weather_data.current_weather.precipitation}mm.
        
        Please provide helpful advice about cherry tomato cultivation based on the user's question.
        Consider the current weather conditions in your response.""" 