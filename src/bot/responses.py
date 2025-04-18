def get_responses():
    return {
        # Categorias básicas
        "saudacao": [
            "Olá! Bem-vindo ao seu assistente culinário! Como posso ajudar hoje?",
            "Oi! Estou aqui para ajudar com suas dúvidas culinárias. O que deseja preparar?",
            "Olá, chef! Procurando alguma receita especial hoje?"
        ],
        "despedida": [
            "Até a próxima! Bom apetite!",
            "Adeus! Espero que sua refeição fique deliciosa!",
            "Tchau! Volte quando quiser descobrir novas receitas!"
        ],
        "agradecimento": [
            "De nada! Cozinhar é um prazer!",
            "Por nada! Espero que a receita fique uma delícia!",
            "Disponível sempre que precisar de inspiração na cozinha!"
        ],
        "duvida": [
            "Não entendi bem. Você quer uma receita específica ou uma sugestão?",
            "Poderia detalhar melhor? Está procurando receitas para qual ocasião?",
            "Hmm, não compreendi. Você quer saber sobre ingredientes ou técnicas de preparo?"
        ],
        # Categorias específicas de culinária
        "receita_geral": [
            "Tenho várias receitas deliciosas! Você prefere algo rápido, saudável ou para impressionar convidados?",
            "Adoraria ajudar com uma receita! Você tem algum ingrediente principal em mente?",
            "Que tipo de prato você gostaria de preparar? Entrada, prato principal ou sobremesa?"
        ],
        "receita_rapida": [
            "Para uma refeição rápida, que tal um macarrão ao alho e óleo? Fica pronto em 15 minutos!",
            "Omelete é sempre uma opção rápida! Bata 2 ovos, adicione temperos e está pronto em 5 minutos.",
            "Uma salada de atum é super rápida: misture atum em lata, tomate, cebola e temperos a gosto."
        ],
        "receita_saudavel": [
            "Para uma refeição saudável, experimente um bowl de quinoa com legumes grelhados e abacate.",
            "Salada de grão-de-bico com tomate, pepino e azeite de oliva é nutritiva e fácil de fazer!",
            "Um salmão grelhado com aspargos é uma excelente opção saudável e rica em nutrientes."
        ],
        "receita_vegetariana": [
            "Para um prato vegetariano delicioso, experimente um curry de grão-de-bico com leite de coco.",
            "Risoto de cogumelos é uma ótima opção vegetariana cheia de sabor!",
            "Berinjela à parmegiana sem carne é um clássico vegetariano que agrada a todos."
        ],
        "receita_lowcarb": [
            "Para uma refeição low carb, experimente um salmão grelhado com legumes assados.",
            "Omelete com espinafre e queijo é uma opção low carb nutritiva e rápida.",
            "Abobrinha recheada com carne moída e queijo é uma delícia low carb!"
        ],
        "tecnica_culinaria": [
            "Para cortar cebola sem chorar, tente colocá-la na geladeira por 30 minutos antes.",
            "Para um arroz soltinho, lave bem os grãos antes de cozinhar para remover o amido.",
            "Para assar carnes uniformemente, deixe-as atingir a temperatura ambiente antes de ir ao forno."
        ],
        "padrao": [
            "Desculpe, não entendi bem. Você poderia perguntar sobre uma receita específica ou ingredientes?",
            "Não tenho certeza do que você precisa. Posso sugerir receitas por categoria ou ingredientes.",
            "Hmm, não captei. Posso ajudar com receitas, dicas culinárias ou sugestões de pratos."
        ],
        # Dados adicionais organizados
        "receitas_detalhes": {
            "frango ao curry": "Receita de Frango ao Curry:\n- 500g de frango em cubos\n- 1 cebola picada\n- 2 dentes de alho\n- 2 colheres de curry em pó\n- 200ml de leite de coco\n- Sal e pimenta a gosto\n\nModo de preparo: Refogue a cebola e o alho, adicione o frango e doure. Adicione o curry, sal, pimenta e por último o leite de coco. Cozinhe por 15-20 minutos em fogo baixo.",
            "strogonoff de frango": "Receita de Strogonoff de Frango:\n- 500g de frango em cubos\n- 1 cebola picada\n- 2 dentes de alho\n- 1 lata de creme de leite\n- 3 colheres de ketchup\n- 3 colheres de mostarda\n- Batata palha para servir\n\nModo de preparo: Refogue a cebola e o alho, adicione o frango e doure. Adicione ketchup, mostarda e deixe cozinhar por 10 minutos. Desligue o fogo e adicione o creme de leite.",
            "salada de frango": "Receita de Salada de Frango:\n- 300g de peito de frango cozido e desfiado\n- Alface, rúcula ou mix de folhas\n- Tomate cereja cortado ao meio\n- Pepino em cubos\n- Cenoura ralada\n- Azeite, sal e limão a gosto\n\nModo de preparo: Misture todos os ingredientes em uma tigela grande. Tempere com azeite, sal e limão."
        },
        "ingredientes": {
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
        },
        "dietas": {
            "vegetariana": ["risoto de cogumelos", "lasanha de berinjela", "curry de grão-de-bico"],
            "vegana": ["estrogonofe de cogumelos", "feijoada vegana", "tofu grelhado com legumes"],
            "sem glúten": ["risoto de camarão", "frango com batata doce", "polenta cremosa"],
            "lowcarb": ["omelete com queijo", "frango com legumes", "salmão com aspargos"],
            "cetogênica": ["ovos mexidos com bacon", "frango com abacate", "carne com manteiga"]
        },
        "sugestoes_pratos": {
            "entrada": ["bruschetta de tomate", "salada caprese", "bolinhos de queijo"],
            "principal": ["lasanha à bolonhesa", "frango assado com batatas", "risoto de cogumelos"],
            "sobremesa": ["mousse de chocolate", "pudim de leite", "torta de limão"]
        }
    }
