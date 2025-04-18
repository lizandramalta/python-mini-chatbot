import random
from .responses import get_responses
import re

class Chatbot:
    def __init__(self):
        self.responses = get_responses()

    def process_input(self, user_input):
        user_input = user_input.lower()

        # Verifica o tipo de mensagem
        if self._is_greeting(user_input):
            return self._get_random_response("saudacao")
        elif self._is_goodbye(user_input):
            return self._get_random_response("despedida")
        elif self._is_thanks(user_input):
            return self._get_random_response("agradecimento")
        elif self._is_question(user_input):
            return self._get_random_response("duvida")
        else:
            return self._get_random_response("padrao")

    def _is_greeting(self, text):
        greetings = ["oi", "olá", "bom dia", "boa tarde", "boa noite", "e aí", "tudo bem"]
        return any(greeting in text for greeting in greetings)

    def _is_goodbye(self, text):
        goodbyes = ["tchau", "adeus", "até mais", "até logo", "até a próxima", "falou"]
        return any(goodbye in text for goodbye in goodbyes)

    def _is_thanks(self, text):
        thanks = ["obrigado", "obrigada", "valeu", "agradeço", "grato", "grata", "thanks"]
        return any(thank in text for thank in thanks)

    def _is_question(self, text):
        return "?" in text or any(word in text for word in ["como", "quando", "onde", "por que", "quem", "qual"])

    def _get_random_response(self, category):
        if category in self.responses:
            return random.choice(self.responses[category])
        return random.choice(self.responses["padrao"])
