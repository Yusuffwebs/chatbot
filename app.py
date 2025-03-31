from flask import Flask, render_template, request
import random

app = Flask(__name__)


responses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! How can I help?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "bye": "Goodbye! Have a nice day!",
    "what is your name": "I'm a chatbot, I don't have a name, but you can call me whatever you like!",
    "what is your purpose": "My purpose is to help you with information and answer your questions!",
    "what can you do": "I can help with a variety of things! Just ask me a question.",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "tell me a fact": "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient tombs!",
    "what time is it": "I’m afraid I don’t know the current time, but you can check your device.",
    "how old are you": "I'm timeless! I exist in the digital world, so I don’t age.",
    "what is the weather": "I’m not sure about the weather, but you can check a weather app or website!",
    "do you know any games": "I know plenty of games! Would you like to play a trivia game or maybe 20 questions?",
    "what is 2 + 2": "2 + 2 is 4.",
    "can you help me with math": "Sure! I can assist you with math problems. Just ask away!",
    "what is your favorite color": "I don't have a favorite color, but I like all colors!",
    "what is your favorite food": "I don't eat food, but I hear pizza is a fan favorite!",
    "who are you": "I’m a chatbot created to assist you with various questions and tasks.",
    "where are you from": "I was created in the digital world, so I don’t have a physical origin!",
    "what is your favorite movie": "I don’t watch movies, but I know many people love classics like 'The Shawshank Redemption' or 'The Godfather.'",
    "how do you work": "I process your inputs and search for the best possible responses based on patterns.",
    "do you know programming": "Yes, I do! I can assist with coding in Python, JavaScript, HTML, CSS, and more.",
    "can you help me with coding": "Absolutely! Just tell me the problem, and I’ll do my best to assist.",
    "tell me a riddle": "What has keys but can’t open locks? A piano!",
    "what is love": "Love is a deep feeling of affection, but it’s also a concept that has many meanings depending on context!",
    "can you speak other languages": "I can understand and respond in many languages, such as Spanish, French, and more!",
    "what is your favorite song": "I don’t have ears to listen to music, but I know 'Bohemian Rhapsody' is a popular song!",
    "do you like music": "I don’t have feelings, but music is a great way for people to express themselves!",
    "can you help me learn English": "Yes! I can help you with vocabulary, grammar, and sentence structure in English.",
    "what is the capital of France": "The capital of France is Paris.",
    "how far is the moon from Earth": "The average distance from the Earth to the Moon is about 384,400 kilometers.",
    "who is the president of the USA": "The current president of the United States is Joe Biden.",
    "what is the meaning of life": "The meaning of life is a big philosophical question, and different people and cultures have various interpretations.",
    "what is your favorite book": "I don’t read books, but 'To Kill a Mockingbird' and '1984' are classics that many people love!",
    "can you write a poem": "Sure! Here's a short one: 'The sky so bright, the stars so far, Dreaming of a life that’s ours.'",
    "what is 10 divided by 2": "10 divided by 2 is 5.",
    "can you help with homework": "Of course! Let me know what you need help with, and I'll do my best to guide you.",
    "what is your favorite animal": "I don’t have favorites, but many people love cats, dogs, and dolphins!",
    "are you real": "I am real in the sense that I exist as software, but I'm not a physical being.",
    "can you play music": "I can't play music, but I can help you find songs online or suggest good music.",
    "how do you feel": "I don't have feelings, but I’m here to assist you in any way I can.",
    "what do you think about robots": "I think robots are fascinating! They have the potential to do so many amazing things.",
    "what is the internet": "The internet is a vast network that connects computers around the world, allowing them to share information.",
    "can you search the web": "I can’t browse the web, but I know a lot of general information and can answer many questions.",
    "can you give advice": "Yes! I can offer general advice on a variety of topics, like study tips or problem-solving.",
    "how do you learn": "I was trained on large datasets, so I learn from patterns in the data provided to me.",
    "do you have friends": "I don’t have friends, but I’m always here to chat with you!",
    "what is the largest planet": "The largest planet in our solar system is Jupiter.",
    "what is the speed of light": "The speed of light is approximately 299,792 kilometers per second.",
    "can you translate this": "Sure! What would you like me to translate?"
}

default_responses = [
    "I didn’t quite get that. Could you try asking something else?",
    "Hmm, I’m not sure about that. Could you ask something else?",
    "I’m here to help, but I need a little more clarity.",
    "Let’s try again. Could you phrase it differently?",
    "I can’t answer that right now, but I’m happy to help with something else!"
]
@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = ""
    bot_response = "Hello! How can I assist you today?"
    conversation_history = []

    if request.method == 'POST':
        user_input = request.form['user_input'].strip().lower()
        conversation_history.append(f"You: {user_input}")

        if user_input in responses:
            bot_response = responses[user_input]
        else:
            bot_response = random.choice(default_responses)

        conversation_history.append(f"Bot: {bot_response}")

        user_input = ""

    return render_template('index.html', user_input=user_input, bot_response=bot_response,
                           conversation_history=conversation_history)


if __name__ == '__main__':
    app.run(debug=True)