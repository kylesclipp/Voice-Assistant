from .time_commands import TimeCommand, DateCommand
from .greeting_commands import GreetCommand, FarewellCommand
from .weather_commands import WeatherCommand
from .gratitude_commands import ThankYouCommand
from .hue_commands import HueCommand
from .alarm_commands import AlarmSetCommand, AlarmListCommand

def get_all_commands():
    return [
        TimeCommand(),
        DateCommand(),
        GreetCommand(),
        FarewellCommand(),
        WeatherCommand(),
        ThankYouCommand(),
        HueCommand(),
        AlarmSetCommand(),
        AlarmListCommand(),
    ]