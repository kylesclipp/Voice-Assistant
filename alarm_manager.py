import datetime
import threading
import time
import winsound

class AlarmManager:
    def __init__(self):
        self.alarms = []
        self.alarm_thread = threading.Thread(target=self._check_alarms, daemon=True)
        self.alarm_thread.start()

    def add_alarm(self, alarm_time):
        self.alarms.append(alarm_time)
        self.alarms.sort()
        print(f"Debug: Alarm added for {alarm_time.strftime('%I:%M %p')}")  # Debug print

    def get_alarms(self):
        return self.alarms.copy()

    def _check_alarms(self):
        while True:
            now = datetime.datetime.now()
            if self.alarms and now >= self.alarms[0]:
                self._trigger_alarm()
                self.alarms.pop(0)
            time.sleep(1)

    def _trigger_alarm(self):
        print("ALARM!")
        for _ in range(5):
            winsound.Beep(1000, 1000)
            time.sleep(0.5)

# Global instance
alarm_manager = AlarmManager()