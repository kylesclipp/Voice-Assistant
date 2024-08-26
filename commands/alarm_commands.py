from .base_command import BaseCommand
import datetime
import re
from alarm_manager import alarm_manager

class AlarmSetCommand(BaseCommand):
    def matches(self, text: str) -> bool:
        alarm_keywords = ["set alarm", "wake me up", "set an alarm", "remind me"]
        return any(keyword in text.lower() for keyword in alarm_keywords)

    def execute(self, entities: dict = None) -> str:
        text = entities.get('raw_text', '').lower()
        alarm_time = self.extract_time(text)
        
        if alarm_time:
            alarm_manager.add_alarm(alarm_time)
            return f"Alarm set for {alarm_time.strftime('%I:%M %p')}"
        else:
            return "I couldn't understand the time for the alarm. Please specify the time in HH:MM AM/PM format."

    def extract_time(self, text: str) -> datetime.datetime:
        # Updated pattern to capture AM/PM more explicitly
        pattern = r'(\d{1,2}):?(\d{2})?\s*(a\.?m\.?|p\.?m\.?)?'
        
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            hour, minute, period = match.groups()
            hour = int(hour)
            minute = int(minute) if minute else 0
            
            is_pm = False
            if period:
                is_pm = period.lower().startswith('p')
            elif hour >= 12:
                is_pm = True

            if is_pm and hour < 12:
                hour += 12
            elif not is_pm and hour == 12:
                hour = 0

            now = datetime.datetime.now()
            alarm_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            
            if alarm_time <= now:
                alarm_time += datetime.timedelta(days=1)
            
            print(f"Debug: Extracted time - {alarm_time.strftime('%I:%M %p')}")  # Debug print
            return alarm_time
        
        print("Debug: No time match found")  # Debug print
        return None

class AlarmListCommand(BaseCommand):
    def matches(self, text: str) -> bool:
        alarm_keywords = ["list alarms", "show alarms", "what alarms"]
        return any(keyword in text.lower() for keyword in alarm_keywords)
    
    def execute(self, entities: dict = None) -> str:
        alarm_list = alarm_manager.get_alarms()
        if not alarm_list:
            return "No alarms set."
            
        alarm_text = "\n".join(alarm.strftime("%I:%M %p") for alarm in alarm_list)
        return f"Alarms:\n{alarm_text}"