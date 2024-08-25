from .base_command import BaseCommand
import random

class GreetCommand(BaseCommand):
    def __init__(self):
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Greetings! How may I help you?",
            "Hey! I'm here if you need anything.",
        ]

    def matches(self, text: str) -> bool:
        greet_keywords = ["hello", "hi", "hey", "greetings"]
        return any(keyword == text.lower().strip() for keyword in greet_keywords)

    def execute(self, entities: dict = None) -> str:
        return random.choice(self.greetings)

class FarewellCommand(BaseCommand):
    def matches(self, text: str) -> bool:
        farewell_keywords = ["goodbye", "bye"]
        return any(keyword == text.lower().strip() for keyword in farewell_keywords)

    def execute(self, entities: dict = None) -> str:
        return "Goodbye! Have a great day!"