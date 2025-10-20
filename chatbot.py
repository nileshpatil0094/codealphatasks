# --- Simple Rule-Based Chatbot ---

def chatbot_response(user_input):
    """Return a predefined response based on user input."""
    user_input = user_input.lower()  # Convert to lowercase for easy matching

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! 👋"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif user_input in ["what is your name", "who are you"]:
        return "I'm ChatBot — your simple Python assistant 🤖."
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day! 👋"
    else:
        return "I'm not sure how to respond to that. Try saying 'hello' or 'bye'."

# --- Main Chat Loop ---
print("🤖 Simple ChatBot (type 'bye' to exit)")
print("---------------------------------------")

while True:
    user = input("You: ")
    response = chatbot_response(user)
    print("Bot:", response)

    if user.lower() in ["bye", "goodbye", "see you"]:
        break