from functools import lru_cache
import logging
from pydantic import Field, computed_field, model_validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    log_level: int = Field(default=logging.DEBUG, alias="LOG_LEVEL")
    tenant_id: str = Field(alias="TENANT_ID")
    frontend_client_id: str = Field(alias="FRONTEND_CLIENT_ID")
    
    backend_api_url: str = Field(default="http://localhost:8001", alias="BACKEND_API_URL")
    backend_api_client_id: str = Field(alias="BACKEND_API_CLIENT_ID")
    backend_api_scope: str = Field(default="user_impersonation", alias="BACKEND_API_SCOPE")
    backend_api_max_token_lifetime: int = Field(default=3600)
    backend_api_token_lifetime_buffer: int = Field(default=100)

    @model_validator(mode="before")
    @classmethod
    def convert_values_before_init(cls, data: dict) -> dict:
        if "LOG_LEVEL" in data:
            data["LOG_LEVEL"] = int(data["LOG_LEVEL"])
        return data
    
    @computed_field
    @property
    def backend_scope_name(self) -> str:
        return f"api://{self.backend_api_client_id}/{self.backend_api_scope}" 
    
    @computed_field
    @property
    def frontend_authority(self) -> str:
        return f"https://login.microsoftonline.com/{self.tenant_id}"


_settings = Settings()


@lru_cache
def get_settings() -> Settings:
    return _settings
