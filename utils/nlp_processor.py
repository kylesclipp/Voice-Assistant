import spacy
from utils.logger import logger

class NLPProcessor:
    def __init__(self):
        self.nlp = None
        self.enabled = False
        try:
            self.nlp = spacy.load("en_core_web_sm")
            self.enabled = True
        except OSError:
            logger.warning("Could not load the spaCy model. NLP processing will be disabled.")

    def process(self, text):
        if not self.enabled:
            return "unknown", {"raw_text": text}

        doc = self.nlp(text)
        
        # Extract key information
        intent = self.extract_intent(doc)
        entities = self.extract_entities(doc)
        entities["raw_text"] = text
        
        return intent, entities

    def extract_intent(self, doc):
        
        greeting_keywords = ["hello", "hi", "hey"]
        if any(token.text.lower() in [greeting_keywords] for token in doc):
            return "greeting"
        
        weather_keywords = ["weather", "temperature", "forecast"]
        if any(token.text.lower() in [weather_keywords] for token in doc):
            return "get_weather"
        
        time_keywords = ["time", "date"]
        if any(token.text.lower() in [time_keywords] for token in doc):
            return "get_time"
        
        gratitude_keywords = ["thank you", "thanks", "appreciate it"]
        if any (token.text.lower() in [gratitude_keywords] for token in doc):
            return "gratitude"
        
        return "unknown"
    


    def extract_entities(self, doc):
        entities = {}
        for ent in doc.ents:
            if ent.label_ == "GPE":  # Geographical Entity
                entities["location"] = ent.text
        return entities