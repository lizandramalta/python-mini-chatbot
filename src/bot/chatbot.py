import random
import re
from .responses import get_responses

class Chatbot:
    def __init__(self):
        self.termos_indecisao = ["não sei", "não tenho ideia", "estou indeciso", "estou indecisa",
                              "me ajude a decidir", "sugestão", "recomendação", "o que sugere",
                              "não sei o que", "estou em dúvida", "dúvida", "não decidi", "qualquer coisa"]

        self.respostas_negativas = ["não", "por enquanto não", "agora não", "ainda não", "nao",
                                   "talvez depois", "deixa pra lá", "não preciso", "tá bom", "ok",
                                   "entendi", "não quero mais", "não quero", "já é suficiente"]
        self.responses = get_responses()
        self.ingredientes = {
            "frango": ["frango ao curry", "strogonoff de frango", "salada de frango"],
            "carne": ["carne de panela", "bife à parmegiana", "estrogonofe de carne"],
            "peixe": ["peixe assado", "moqueca de peixe", "sushi caseiro"],
            "tomate": ["molho de tomate caseiro", "salada caprese", "gazpacho"],
            "batata": ["batata recheada", "purê de batata", "batata rosti"],
            "arroz": ["risoto", "arroz de forno", "arroz carreteiro"],
            "feijão": ["feijoada", "feijão tropeiro", "salada de feijão"],
            "ovo": ["omelete", "ovos mexidos", "ovo pochê"],
            "macarrão": ["macarrão ao molho branco", "espaguete à bolonhesa", "macarrão com atum"],
            "legumes": ["legumes assados", "sopa de legumes", "ratatouille"]
        }
        self.dietas = {
            "vegetariana": ["risoto de cogumelos", "lasanha de berinjela", "curry de grão-de-bico"],
            "vegana": ["estrogonofe de cogumelos", "feijoada vegana", "tofu grelhado com legumes"],
            "sem glúten": ["risoto de camarão", "frango com batata doce", "polenta cremosa"],
            "lowcarb": ["omelete com queijo", "frango com legumes", "salmão com aspargos"],
            "cetogênica": ["ovos mexidos com bacon", "frango com abacate", "carne com manteiga"]
        }
        # Adiciona detalhes de receitas para quando o usuário pedir mais informações
        self.receitas_detalhes = {
            "frango ao curry": "Receita de Frango ao Curry:\n- 500g de frango em cubos\n- 1 cebola picada\n- 2 dentes de alho\n- 2 colheres de curry em pó\n- 200ml de leite de coco\n- Sal e pimenta a gosto\n\nModo de preparo: Refogue a cebola e o alho, adicione o frango e doure. Adicione o curry, sal, pimenta e por último o leite de coco. Cozinhe por 15-20 minutos em fogo baixo.",
            "strogonoff de frango": "Receita de Strogonoff de Frango:\n- 500g de frango em cubos\n- 1 cebola picada\n- 2 dentes de alho\n- 1 lata de creme de leite\n- 3 colheres de ketchup\n- 3 colheres de mostarda\n- Batata palha para servir\n\nModo de preparo: Refogue a cebola e o alho, adicione o frango e doure. Adicione ketchup, mostarda e deixe cozinhar por 10 minutos. Desligue o fogo e adicione o creme de leite.",
            "salada de frango": "Receita de Salada de Frango:\n- 300g de peito de frango cozido e desfiado\n- Alface, rúcula ou mix de folhas\n- Tomate cereja cortado ao meio\n- Pepino em cubos\n- Cenoura ralada\n- Azeite, sal e limão a gosto\n\nModo de preparo: Misture todos os ingredientes em uma tigela grande. Tempere com azeite, sal e limão."
        }

        # Sistema de memória e contexto de conversa
        self.ultima_conversa = {
            "receitas_mencionadas": [],
            "ingrediente_atual": None,
            "dieta_atual": None,
            "ultima_pergunta": None,  # Para lembrar a última pergunta feita
            "ultima_receita": None   # Para lembrar a última receita mencionada
        }

        # Sugestões padrão para diferentes tipos de pratos
        self.sugestoes_pratos = {
            "entrada": ["bruschetta de tomate", "salada caprese", "bolinhos de queijo"],
            "principal": ["lasanha à bolonhesa", "frango assado com batatas", "risoto de cogumelos"],
            "sobremesa": ["mousse de chocolate", "pudim de leite", "torta de limão"]
        }

        # Para identificar feedback positivo/negativo
        self.feedback_positivo = ["legal", "gostei", "ótimo", "perfeito", "bom", "show", "bacana", "top", "adorei", "maravilha"]
        self.feedback_negativo = ["não gostei", "ruim", "péssimo", "horrível", "não curti", "não é isso", "não quero"]

    def process_input(self, user_input):
        user_input = user_input.lower()

        # NOVA VERIFICAÇÃO - coloque-a logo no início do process_input
        # Verifica se é uma resposta negativa após qualquer pergunta do chatbot
        if any(negativa in user_input for negativa in self.respostas_negativas):
            # Se for após feedback positivo de receita, oferece encerrar o assunto
            if self.ultima_conversa.get("ultima_receita"):
                self.ultima_conversa["ultima_pergunta"] = None
                self.ultima_conversa["ultima_receita"] = None
                return "Tudo bem! Se precisar de mais alguma receita ou dica culinária, é só me perguntar. Posso ajudar com mais alguma coisa?"
            # Se for em outro contexto
            elif self.ultima_conversa.get("ultima_pergunta"):
                self.ultima_conversa["ultima_pergunta"] = None
                return "Sem problemas! Estou aqui para ajudar quando quiser. Posso auxiliar com receitas, dicas de preparo ou sugestões de pratos."

        # 1. Verifica se é um feedback positivo após uma receita
        if any(termo in user_input for termo in self.feedback_positivo) and self.ultima_conversa["ultima_receita"]:
            return "Que bom que gostou! Quer saber mais alguma receita ou tem outro ingrediente em mente?"

        # 2. Verifica se é um feedback negativo após uma receita
        if any(termo in user_input for termo in self.feedback_negativo) and self.ultima_conversa["ultima_receita"]:
            return "Desculpe por isso. Posso sugerir outra receita? Tem algum outro ingrediente que prefere?"

        # NOVA VERIFICAÇÃO - logo após verificar feedback
        # Verifica se o usuário está indeciso (mesmo sem uma pergunta anterior)
        if any(termo in user_input for termo in self.termos_indecisao):
            self.ultima_conversa["ultima_pergunta"] = "tipo_prato"
            return "Entendi que você está indeciso! Posso sugerir por categoria ou por ingrediente. Você prefere uma entrada, prato principal ou sobremesa? Ou prefere que eu sugira algo com um ingrediente específico?"

        # 1. Verifica se é um feedback positivo após uma receita
        if any(termo in user_input for termo in self.feedback_positivo) and self.ultima_conversa["ultima_receita"]:
            return "Que bom que gostou! Quer saber mais alguma receita ou tem outro ingrediente em mente?"

        # 3. Verifica se está solicitando uma receita específica
        for receita in self.receitas_detalhes.keys():
            if receita.lower() in user_input:
                self.ultima_conversa["ultima_receita"] = receita
                return self.receitas_detalhes[receita]

        # 4. Verifica se está pedindo detalhes sobre a última receita
        if any(palavra in user_input for palavra in ["detalhe", "como faz", "receita completa", "modo de preparo", "ingredientes"]):
            if self.ultima_conversa["receitas_mencionadas"]:
                for receita in self.ultima_conversa["receitas_mencionadas"]:
                    if receita in self.receitas_detalhes:
                        self.ultima_conversa["ultima_receita"] = receita
                        return self.receitas_detalhes[receita]
                return "Sobre qual receita você gostaria de mais detalhes?"

        # 5. Verifica se é uma resposta a uma pergunta sobre tipo de prato
        if self.ultima_conversa["ultima_pergunta"] == "tipo_prato":
            for tipo, pratos in self.sugestoes_pratos.items():
                if tipo in user_input or self._is_similar(tipo, user_input):
                    self.ultima_conversa["ultima_pergunta"] = None
                    return f"Para {tipo}, sugiro: {', '.join(pratos)}. Algum destes te interessa?"

        # 6. Verifica se o usuário está dizendo que não tem preferências
        if any(termo in user_input for termo in ["não sei", "não tenho", "tanto faz", "qualquer um", "não"]) and self.ultima_conversa["ultima_pergunta"]:
            self.ultima_conversa["ultima_pergunta"] = None
            return "Sem problema! Aqui estão algumas sugestões populares: frango ao curry, lasanha, risoto de cogumelos. Alguma dessas te interessa?"

        # 7. Verifica se é uma saudação
        if self._is_greeting(user_input):
            return self._get_random_response("saudacao")

        # 8. Verifica se é uma despedida
        elif self._is_goodbye(user_input):
            return self._get_random_response("despedida")

        # 9. Verifica se é um agradecimento
        elif self._is_thanks(user_input):
            return self._get_random_response("agradecimento")

        # 10. Verifica se é uma pergunta sobre receita rápida
        elif self._is_quick_recipe(user_input):
            return self._get_random_response("receita_rapida")

        # 11. Verifica se é uma pergunta sobre receita saudável
        elif self._is_healthy_recipe(user_input):
            return self._get_random_response("receita_saudavel")

        # 12. Verifica se é uma pergunta sobre receita vegetariana
        elif self._is_vegetarian_recipe(user_input):
            return self._get_random_response("receita_vegetariana")

        # 13. Verifica se é uma pergunta sobre receita low carb
        elif self._is_lowcarb_recipe(user_input):
            return self._get_random_response("receita_lowcarb")

        # 14. Verifica se pergunta sobre técnica culinária
        elif self._is_cooking_technique(user_input):
            return self._get_random_response("tecnica_culinaria")

        # 15. Verifica se pergunta sobre receita com ingrediente específico
        elif ingrediente := self._get_ingredient(user_input):
            receitas = self.ingredientes.get(ingrediente, [])
            if receitas:
                # Guarda na memória
                self.ultima_conversa["ingrediente_atual"] = ingrediente
                self.ultima_conversa["receitas_mencionadas"] = receitas
                return f"Com {ingrediente}, você pode fazer: {', '.join(receitas)}. Qual dessas receitas você gostaria de saber mais?"
            return f"Não tenho receitas específicas com {ingrediente}, mas posso sugerir outras opções. Você prefere algo rápido ou saudável?"

        # 16. Verifica se pergunta sobre dieta específica
        elif dieta := self._get_diet(user_input):
            receitas = self.dietas.get(dieta, [])
            if receitas:
                # Guarda na memória
                self.ultima_conversa["dieta_atual"] = dieta
                self.ultima_conversa["receitas_mencionadas"] = receitas
                return f"Para uma dieta {dieta}, recomendo: {', '.join(receitas)}. Gostaria da receita completa de alguma delas?"
            return f"Não tenho receitas específicas para dieta {dieta}. Mas posso sugerir algumas opções saudáveis se quiser."

        # 17. Verifica se é uma pergunta sobre receitas em geral
        elif "sugestão" in user_input or "sugestões" in user_input or self._is_recipe_question(user_input):
            self.ultima_conversa["ultima_pergunta"] = "tipo_prato"
            return "Que tipo de prato você gostaria de preparar? Entrada, prato principal ou sobremesa?"

        # 18. Se nada for identificado
        return self._get_random_response("padrao")

    # Métodos existentes
    def _is_greeting(self, text):
        greetings = ["olá", "oi", "bom dia", "boa tarde", "boa noite", "e aí", "oi, tudo bem", "tudo bem", "ola"]
        return any(greeting in text for greeting in greetings) or text in ["oi", "olá", "ola", "ei", "hey"]

    # Novo método para verificar similaridade entre strings
    def _is_similar(self, word1, word2):
        # Verifica se word2 está contido em word1 ou vice-versa
        if word1 in word2 or word2 in word1:
            return True
        # Verifica se são abreviações
        if len(word1) > 3 and len(word2) > 2 and word1[:3] == word2[:3]:
            return True
        return False

    # Restante dos métodos permanecem iguais
    def _is_goodbye(self, text):
        goodbyes = ["tchau", "adeus", "até mais", "até logo", "até a próxima", "xau"]
        return any(goodbye in text for goodbye in goodbyes)

    def _is_thanks(self, text):
        thanks = ["obrigado", "obrigada", "valeu", "agradeço", "muito obrigado", "muito obrigada", "obg"]
        return any(thank in text for thank in thanks)

    def _is_quick_recipe(self, text):
        quick_terms = ["rápida", "rápido", "pressa", "urgente", "pouco tempo", "correria", "minutos", "expressa"]
        return any(term in text for term in quick_terms) and self._is_recipe_question(text)

    def _is_healthy_recipe(self, text):
        healthy_terms = ["saudável", "fit", "fitness", "dieta", "light", "sem gordura", "nutritiva", "nutrição", "saudavel"]
        return any(term in text for term in healthy_terms) and self._is_recipe_question(text)

    def _is_vegetarian_recipe(self, text):
        vegetarian_terms = ["vegetariana", "vegetariano", "sem carne", "veggie"]
        return any(term in text for term in vegetarian_terms) and self._is_recipe_question(text)

    def _is_lowcarb_recipe(self, text):
        lowcarb_terms = ["lowcarb", "low carb", "low-carb", "baixo carboidrato", "sem carboidrato", "pouco carboidrato", "keto", "cetogênica"]
        return any(term in text for term in lowcarb_terms) and self._is_recipe_question(text)

    def _is_cooking_technique(self, text):
        technique_terms = ["como fazer", "como preparar", "técnica", "dica", "segredo", "truque", "melhor forma"]
        return any(term in text for term in technique_terms)

    def _get_ingredient(self, text):
        for ingrediente in self.ingredientes.keys():
            if ingrediente in text:
                return ingrediente
        return None

    def _get_diet(self, text):
        for dieta in self.dietas.keys():
            if dieta in text:
                return dieta
        return None

    def _is_recipe_question(self, text):
        recipe_terms = ["receita", "prato", "comida", "cozinhar", "preparar", "fazer", "sugestão", "ideia", "refeição"]
        return any(term in text for term in recipe_terms)

    def _get_random_response(self, category):
        return random.choice(self.responses.get(category, self.responses["padrao"]))
