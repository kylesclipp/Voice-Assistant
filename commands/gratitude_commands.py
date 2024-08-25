from .base_command import BaseCommand
import random

class ThankYouCommand(BaseCommand):
    def __init__(self):
        self.responses = [
            "You're welcome!",
            "No problem at all!",
            "Glad I could help!",
            "Anytime!",
            "My pleasure!",
        ]

    def matches(self, text: str) -> bool:
        gratitude_keywords = ["thanks", "thank you", "appreciate it"]
        return any(keyword in text.lower() for keyword in gratitude_keywords)

    def execute(self, entities: dict = None) -> str:
        return random.choice(self.responses)