from abc import ABC, abstractmethod

from pydantic import BaseModel, Field, computed_field

from src.settings import Settings


class BaseAPIToken(BaseModel):
    value: str
    username: str
    user_id: str
    lifetime_start: int
    lifetime_end: int
    max_lifetime: int 
    lifetime_buffer: int

    @property
    @abstractmethod
    def is_expired(self) -> bool:
        pass

    @classmethod
    @abstractmethod
    def from_signed_in_user(cls, settings: Settings) -> "BaseAPIToken":
        pass
