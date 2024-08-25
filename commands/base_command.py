from abc import ABC, abstractmethod

class BaseCommand(ABC):
    @abstractmethod
    def matches(self, text: str) -> bool:
        pass

    @abstractmethod
    def execute(self, entities: dict = None) -> str:
        pass