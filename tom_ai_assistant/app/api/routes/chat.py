from fastapi import APIRouter, HTTPException
from app.models.schemas import UserMessage, ChatResponse
from app.services.weather_service import WeatherService
from app.services.ai_service import AIService

router = APIRouter()
weather_service = WeatherService()
ai_service = AIService()

@router.post("/chat", response_model=ChatResponse)
async def chat_with_tomato_expert(user_message: UserMessage) -> ChatResponse:
    try:
        # Get weather data
        weather_data = weather_service.get_weather_data()
        
        # Generate AI response
        response = ai_service.generate_response(
            user_message=user_message.message,
            weather_data=weather_data
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 