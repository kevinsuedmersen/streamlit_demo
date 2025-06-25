from abc import ABC, abstractmethod

from src.settings import Settings
from src.api_tokens import BaseAPIToken


class BaseAPIClient(ABC):
    @abstractmethod
    def _get_api_token(self) -> BaseAPIToken:
        pass

    @abstractmethod
    def _get_headers(self) -> dict:
        pass

    @abstractmethod
    def test_connection(self) -> bool:
        pass
