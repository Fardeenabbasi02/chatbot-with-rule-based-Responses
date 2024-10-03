def chatbot_response(user_input):
    # Convert input to lower case for easier matching
    user_input = user_input.lower()

    # Basic greetings
    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I assist you today?"

    # Farewell
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye! Have a great day!"

    # Asking for help
    elif "help" in user_input:
        return "I'm here to help! What do you need assistance with?"

    # Asking about the weather
    elif "weather" in user_input:
        return "I can't check the weather, but you can try searching online or using a weather app."

    # Default response for unrecognized inputs
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"

# Main loop to interact with the chatbot
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")

    # Exit loop if the user says goodbye
    if user_input.lower() in ["bye", "goodbye"]:
        break