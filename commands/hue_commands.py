from .base_command import BaseCommand
from phue import Bridge
import json

class HueCommand(BaseCommand):
    def __init__(self):
        self.bridge_ip = "10.0.0.30"  # Replace with your actual bridge IP
        self.bridge = Bridge(self.bridge_ip)

        # The first time this runs, press the button on the bridge and run the script within 30 seconds
        self.bridge.connect()

        # Get all the lights
        self.lights = self.bridge.get_light_objects('name')

        # Define room-light mappings
        self.room_lights = {
            "Kyle's Room": ["Kyle's Lamp"],
            # Add more rooms and their corresponding light names
        }

    def matches(self, text: str) -> bool:
        light_keywords = ["light", "lights", "hue"]
        action_keywords = ["on", "off", "turn"]
        return any(keyword in text.lower() for keyword in light_keywords) and \
               any(keyword in text.lower() for keyword in action_keywords)

    def execute(self, entities: dict = None) -> str:
        text = entities.get('raw_text', '').lower()
        
        # Determine the action (on or off)
        if "on" in text:
            action = True
            action_text = "on"
        elif "off" in text:
            action = False
            action_text = "off"
        else:
            return "I'm not sure what you want to do with the lights."

        # Always target Kyle's Lamp
        target_lights = ["Kyle's Lamp"]

        # Perform the action on the target lights
        for light_name in target_lights:
            if light_name in self.lights:
                self.lights[light_name].on = action

        return f"Kyle's Lamp turned {action_text}."