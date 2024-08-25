from .base_command import BaseCommand
import requests
from config import api_config

class WeatherCommand(BaseCommand):
    def matches(self, text: str) -> bool:
        weather_keywords = ["weather", "temperature", "forecast", "how's it outside", "is it raining"]
        return any(keyword in text.lower() for keyword in weather_keywords)

    def execute(self, entities=None) -> str:
        api_key = api_config.OPENWEATHERMAP_API_KEY
        city = entities.get('location', 'New York')  # Default to New York if no location is specified
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
            
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            return f"The weather in {city} is {description} with a temperature of {temp}°C"
        except requests.RequestException as e:
            return f"Sorry, I couldn't fetch the weather information at the moment. Error: {str(e)}"