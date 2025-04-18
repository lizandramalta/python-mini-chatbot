from bot.chatbot import Chatbot

def main():
    chatbot = Chatbot()
    print("Chatbot: Olá! Digite 'sair' quando quiser encerrar a conversa.")

    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Chatbot: Até mais! Tenha um bom dia!")
            break

        response = chatbot.process_input(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
