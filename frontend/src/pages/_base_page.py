from abc import ABC, abstractmethod

from src.settings import Settings


class BasePage(ABC):
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @abstractmethod
    def display(self) -> None:
        pass
