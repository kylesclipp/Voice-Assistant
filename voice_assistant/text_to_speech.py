import pyttsx3
import settings

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', settings.VOICE_RATE)
        self.engine.setProperty('volume', settings.VOICE_VOLUME)

    def speak(self, text):
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()