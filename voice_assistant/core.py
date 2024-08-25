import random
from .speech_recognition import SpeechRecognizer
from .text_to_speech import TextToSpeech
from commands import get_all_commands
from utils.nlp_processor import NLPProcessor
from utils.context_manager import ContextManager
import settings

class VoiceAssistant:
    def __init__(self):
        self.recognizer = SpeechRecognizer()
        self.speaker = TextToSpeech()
        self.commands = get_all_commands()
        self.nlp_processor = NLPProcessor()
        self.context_manager = ContextManager()

    def run(self):
        while True:
            text = self.recognizer.listen()
            if text:
                self.process_input(text)

    def process_input(self, text):
        intent, entities = self.nlp_processor.process(text)
        
        # Use context if needed
        if self.nlp_processor.enabled:
            context = self.context_manager.get_context("last_intent")
            if context and intent == "unknown":
                intent = context

        command_executed = False
        for command in self.commands:
            if command.matches(text):
                response = command.execute(entities)
                self.speaker.speak(response)
                if self.nlp_processor.enabled:
                    self.context_manager.set_context("last_intent", intent)
                command_executed = True
                break

        if not command_executed:
            self.handle_unknown_command(text)

    def handle_unknown_command(self, text):
        response = random.choice(settings.UNKNOWN_COMMAND_RESPONSES)
        self.speaker.speak(response)