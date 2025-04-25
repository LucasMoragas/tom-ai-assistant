# app/config/settings.py

from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # OpenAI
    OPENAI_API_KEY: str
    # ASSISTANT_ID: str  # optional, can be saved after creation

    # FastAPI
    APP_NAME: str = "Tom - AI Assistant"
    DEBUG: bool = True

    # Other options (example)
    API_V1_PREFIX: str = "/api/v1"
    TIMEOUT_SECONDS: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Cache to avoid reprocessing on each import
@lru_cache()
def get_settings():
    return Settings()
