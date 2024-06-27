def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hi": "Hello! How can I assist you today?",
        "how are you": "I'm just a bot, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "help": "I can assist you with basic queries. Ask me something.",
        "what is your name": "I'm just a chatbot.",
        "what can you do": "I can respond to basic queries. Try asking something.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "who created you": "I was created by kunal.",
        "where are you from": "I exist in the cloud.",
        "thank you": "You're welcome!",
        "default": "I'm sorry, I don't understand that ?"
    }


    if user_input in responses:
        return responses[user_input]
    else:
        return responses["default"]

def main():
    print("Welcome! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(chatbot_response(user_input))
            break
        else:
            print("Bot:", chatbot_response(user_input))

if __name__ == "__main__":
    main()
