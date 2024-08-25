from .speech_recognition import SpeechRecognizer
from .text_to_speech import TextToSpeech
from commands import get_all_commands
import random
import settings

class VoiceAssistant:
    def __init__(self):
        self.recognizer = SpeechRecognizer()
        self.speaker = TextToSpeech()
        self.commands = get_all_commands()

    def run(self):
        while True:
            text = self.recognizer.listen()
            if text:
                self.process_input(text)

    def process_input(self, text):
        for command in self.commands:
            if command.matches(text):
                response = command.execute({'raw_text': text})
                self.speaker.speak(response)
                return

        self.handle_unknown_command(text)

    def handle_unknown_command(self, text):
        response = random.choice(settings.UNKNOWN_COMMAND_RESPONSES)
        self.speaker.speak(response)