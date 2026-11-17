# CodeAlpha - Basic Chatbot
# A simple chatbot built with if-else statements.
# It listens to what you type, matches it with answers it knows,
# and replies. If it does not know the answer, it says so.

print("Bot: Hello! I am a simple chatbot. Type 'bye' to stop.")

while True:
    user = input("You: ").lower()  # listen, and make all letters small

    if "hello" in user:
        print("Bot: Hello! How can I help you?")
    elif "how are you" in user:
        print("Bot: I am fine, thank you!")
    elif "your name" in user:
        print("Bot: My name is ChatBot.")
    elif "bye" in user:
        print("Bot: Goodbye! See you again.")
        break  # stop the loop and end the chat
    else:
        print("Bot: Sorry, I don't understand.")
