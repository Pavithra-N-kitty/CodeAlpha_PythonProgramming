print("--- Welcome to the Smart Chatbot! ---")
print("Type 'bye' to exit the conversation.\n")

while True:
    user_input = input("You: ").lower().strip()
    
    # Rule-based logic using simple if-elif checks
    if user_input == "hello" or user_input == "hi":
        print("Chatbot: Hi there! How can I help you today?")
        
    elif "how are you" in user_input:
        print("Chatbot: I'm just a computer script, but I'm functioning perfectly! Thanks for asking.")
        
    elif "your name" in user_input:
        print("Chatbot: I am your CodeAlpha assistant chatbot.")
        
    elif user_input == "bye" or user_input == "exit":
        print("Chatbot: Goodbye! Have a wonderful day ahead!")
        break
        
    else:
        print("Chatbot: I am a basic bot. I don't understand that yet, but I am learning!")
