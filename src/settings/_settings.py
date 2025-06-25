from functools import lru_cache
import logging
from pydantic import Field, computed_field, model_validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    log_level: int = Field(default=logging.DEBUG, alias="LOG_LEVEL")
    backend_api_url: str = Field(default="http://localhost:8001", alias="BACKEND_API_URL")


_settings = Settings()


@lru_cache
def get_settings() -> Settings:
    return _settings
