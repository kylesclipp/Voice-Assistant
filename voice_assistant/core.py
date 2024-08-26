from .speech_recognition import SpeechRecognizer
from .text_to_speech import TextToSpeech
from commands import get_all_commands
import random
import settings
import time

class VoiceAssistant:
    def __init__(self):
        self.recognizer = SpeechRecognizer()
        self.speaker = TextToSpeech()
        self.commands = get_all_commands()
        self.wake_words = ["help me", "hey assistant", "ok al"]
        self.command_timeout = 30  # This could also be moved to settings if you want

    def run(self):
        print("Voice Assistant is ready. Start speaking...")
        listening_until = 0
        while True:
            current_time = time.time()
            if current_time > listening_until:
                text = self.recognizer.listen()
                if text:
                    lower_text = text.lower()
                    if any(wake_word in lower_text for wake_word in self.wake_words):
                        listening_until = current_time + self.command_timeout
                        print("Wake word recognized. Listening for commands...")
                        self.speaker.speak("How can I help you?")
                        continue
                    else:
                        print(f"Ignored: {text}")
            else:
                text = self.recognizer.listen(timeout=listening_until - current_time)
                if text:
                    print(f"You said: {text}")
                    if self.process_input(text):
                        listening_until = time.time() + self.command_timeout
                    else:
                        print("Command not recognized. Still listening...")

    def process_input(self, text):
        for command in self.commands:
            if command.matches(text):
                response = command.execute({'raw_text': text})
                self.output_response(response)
                return True
        self.handle_unknown_command(text)
        return False

    def handle_unknown_command(self, text):
        response = random.choice(settings.UNKNOWN_COMMAND_RESPONSES)
        self.output_response(response)

    def output_response(self, response):
        print(f"Assistant: {response}")
        self.speaker.speak(response)