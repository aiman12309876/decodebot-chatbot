import random
import time

responses = {

    "hello": ["Hello! Welcome to DecodeLabs. How can I assist you today?", 
              "Hi there! Great to see you. What brings you here?",
              "Hey! Ready to learn some AI?"],
    
    "hi": ["Hi! Welcome to DecodeLabs.", 
           "Hello! How can I help you with your AI journey?"],
    
    "hey": ["Hey there! What can I do for you today?",
            "Hello! Ready to build something amazing?"],
    
    "good morning": ["Good morning! Hope you're having a great day!",
                     "Morning! Let's make today productive."],
    
    "good evening": ["Good evening! How was your day?",
                     "Evening! Ready to dive into AI?"],
    
    "good night": ["Good night! Sleep well and see you tomorrow.",
                   "Night! Take rest and come back stronger."],
    
    "bye": ["Goodbye! Keep learning and building. See you soon!",
            "Bye! Remember, every expert was once a beginner.",
            "See you later! Keep coding!"],
    
    "exit": ["Exiting the chat. Goodbye!",
             "Leaving so soon? Come back anytime. Goodbye!"],
    
    "quit": ["Quitting... See you next time!",
             "Goodbye! Stay curious."],
    
    "what is your name": ["I'm DecodeBot, your AI assistant from DecodeLabs!",
                         "I'm your friendly chatbot built with Python. Call me DecodeBot!"],
    
    "who created you": ["I was created by the team at DecodeLabs to help interns learn AI.",
                       "The amazing people at DecodeLabs built me!"],
    
    "what can you do": ["I can chat with you, answer basic questions, and help you understand rule-based AI.",
                       "I'm a rule-based chatbot - I respond to specific inputs. Try saying 'hello' or 'help'!"],
    
    "help": ["I can respond to greetings, tell you about myself, and chat with you. Try saying 'hello' or 'what is your name'.",
             "You can ask me anything! I understand greetings, farewells, and general chat. Just type and I'll respond!"],
    
    "how are you": ["I'm great! Just processing code and helping interns. How about you?",
                    "I'm doing well, thanks for asking! Hope you're having a good day too."],
    
    "i am fine": ["That's great to hear!",
                  "Wonderful! Keep that energy for your projects."],
    
    "i am good": ["Awesome! Let's build something amazing today.",
                  "Good to know! Stay positive and keep learning."],
    
    "i am sad": ["Oh no! Don't worry, you can do this. Take a break and come back stronger.",
                 "Sad? Remember, debugging is part of the journey. You've got this!"],
    
    "what is ai": ["AI (Artificial Intelligence) is the simulation of human intelligence in machines.",
                  "AI is a field of computer science that creates intelligent systems that can learn and make decisions."],
    
    "what is machine learning": ["Machine Learning is a subset of AI where computers learn from data without being explicitly programmed.",
                                "ML helps computers find patterns in data and make predictions."],
    
    "what is python": ["Python is a powerful programming language widely used in AI and data science.",
                      "Python is great for AI because it's simple and has many libraries like TensorFlow and PyTorch."],
    
    "tell me a joke": ["Why do programmers prefer dark mode? Because light attracts bugs!",
                       "What do you call a fake noodle? An impasta!",
                       "Why did the AI break up with the robot? It had no 'connection'."],
    
    "thank you": ["You're welcome! Happy to help.",
                  "Anytime! That's what I'm here for.",
                  "My pleasure! Keep learning and building."],
    
    "thanks": ["You're welcome! 😊",
               "No problem! Always here to help."],
    
    "default": ["I'm not sure I understand that. Can you rephrase?",
                "Hmm, I don't know how to respond to that yet. Try saying 'help' to see what I can do.",
                "Interesting! I'm still learning. Could you simplify that?",
                "I didn't quite get that. Maybe try a different way?"]
}


def get_response(user_input):
    
    user_input = user_input.lower().strip()
    
    if "hello" in user_input:
        return random.choice(responses["hello"])
    elif "hi" in user_input:
        return random.choice(responses["hi"])
    elif "hey" in user_input:
        return random.choice(responses["hey"])
    elif "good morning" in user_input:
        return random.choice(responses["good morning"])
    elif "good evening" in user_input:
        return random.choice(responses["good evening"])
    elif "good night" in user_input:
        return random.choice(responses["good night"])
    
    elif "bye" in user_input:
        return random.choice(responses["bye"])
    elif "exit" in user_input:
        return random.choice(responses["exit"])
    elif "quit" in user_input:
        return random.choice(responses["quit"])
    
    elif "your name" in user_input:
        return random.choice(responses["what is your name"])
    elif "who created you" in user_input or "who made you" in user_input:
        return random.choice(responses["who created you"])
    elif "what can you do" in user_input:
        return random.choice(responses["what can you do"])
    
    elif "help" in user_input:
        return random.choice(responses["help"])
    
    elif "how are you" in user_input:
        return random.choice(responses["how are you"])
    elif "i am fine" in user_input or "i'm fine" in user_input:
        return random.choice(responses["i am fine"])
    elif "i am good" in user_input or "i'm good" in user_input:
        return random.choice(responses["i am good"])
    elif "i am sad" in user_input or "i'm sad" in user_input:
        return random.choice(responses["i am sad"])
    
    elif "what is ai" in user_input or "what is artificial intelligence" in user_input:
        return random.choice(responses["what is ai"])
    elif "machine learning" in user_input or "what is ml" in user_input:
        return random.choice(responses["what is machine learning"])
    elif "python" in user_input:
        return random.choice(responses["what is python"])
    
    elif "joke" in user_input or "funny" in user_input:
        return random.choice(responses["tell me a joke"])
    
    elif "thank" in user_input:
        return random.choice(responses["thank you"])
    
    else:
        return random.choice(responses["default"])


def chatbot():
    
    print("\n" + "=" * 60)
    print("WELCOME TO DECODEBOT".center(60))
    print("=" * 60)
    print("Type 'bye' or 'exit' to quit")
    print("Type 'help' to see what I can do")
    print("=" * 60 + "\n")
    
    print("Bot: Hello! I'm DecodeBot from DecodeLabs. How can I help you today?\n")
    
    while True:
        
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print(f"Bot: {random.choice(responses['bye'])}")
            print("\n" + "=" * 60)
            print("Thanks for chatting with DecodeBot!".center(60))
            print("=" * 60 + "\n")
            break
        
        response = get_response(user_input)
        time.sleep(0.5)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    chatbot()