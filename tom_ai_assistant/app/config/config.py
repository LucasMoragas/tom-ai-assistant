# app/config/settings.py

from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # OpenAI
    OPENAI_API_KEY: str
    # ASSISTANT_ID: str  # opcional, pode ser salvo depois de criado

    # FastAPI
    APP_NAME: str = "Tom - Assistente IA"
    DEBUG: bool = True

    # Outras opções (exemplo)
    API_V1_PREFIX: str = "/api/v1"
    TIMEOUT_SECONDS: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Cache para não reprocessar a cada importação
@lru_cache()
def get_settings():
    return Settings()
