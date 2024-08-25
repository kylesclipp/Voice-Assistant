from .base_command import BaseCommand
import requests

class WeatherCommand(BaseCommand):
    def matches(self, text: str) -> bool:
        return "weather" in text.lower()

    def execute(self) -> str:
        # This is a placeholder. You'd need to sign up for a weather API service
        # and replace this with an actual API call
        api_key = "YOUR_API_KEY"
        city = "New York"  # You could make this dynamic based on user input
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            return f"The weather in {city} is {description} with a temperature of {temp}°C"
        else:
            return "Sorry, I couldn't fetch the weather information at the moment."