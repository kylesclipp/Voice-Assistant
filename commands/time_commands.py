from .base_command import BaseCommand
import datetime

class TimeCommand(BaseCommand):
    def matches(self, text: str) -> bool:
        time_keywords = ["what time", "current time", "time now"]
        return any(keyword in text.lower() for keyword in time_keywords)

    def execute(self, entities: dict = None) -> str:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"

class DateCommand(BaseCommand):
    def matches(self, text: str) -> bool:
        date_keywords = ["what date", "current date", "date today"]
        return any(keyword in text.lower() for keyword in date_keywords)

    def execute(self, entities: dict = None) -> str:
        current_date = datetime.date.today().strftime("%B %d, %Y")
        return f"Today's date is {current_date}"