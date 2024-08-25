import speech_recognition as sr
import settings
from settings import ENERGY_THRESHOLD, DYNAMIC_ENERGY_THRESHOLD

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = ENERGY_THRESHOLD
        self.recognizer.dynamic_energy_threshold = DYNAMIC_ENERGY_THRESHOLD

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=settings.LISTENING_TIMEOUT, phrase_time_limit=settings.PHRASE_TIME_LIMIT)
                text = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {text}")
                return text
            except sr.WaitTimeoutError:
                print("Listening timed out. No speech detected.")
            except sr.UnknownValueError:
                print("Speech was unintelligible")
            except sr.RequestError as e:
                print(f"Could not request results from speech recognition service; {e}")
        return None