import speech_recognition as sr
import settings

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = settings.ENERGY_THRESHOLD
        self.recognizer.dynamic_energy_threshold = settings.DYNAMIC_ENERGY_THRESHOLD

    def listen(self, timeout=None):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, 
                                               timeout=timeout or settings.LISTENING_TIMEOUT, 
                                               phrase_time_limit=settings.PHRASE_TIME_LIMIT)
                text = self.recognizer.recognize_google(audio).lower()
                return text
            except sr.WaitTimeoutError:
                print("Listening timed out.")
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that.")
            except sr.RequestError as e:
                print(f"Could not request results from speech recognition service; {e}")
        return None