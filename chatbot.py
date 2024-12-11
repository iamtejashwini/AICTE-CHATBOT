from flask import Flask, request, jsonify, render_template_string

# Initialize the Flask application
app = Flask(__name__)

# Sample data for responses
responses = {
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "bye": "Goodbye! Have a great day!",
    "what is your name": "I'm Tony's Chatbot, here to assist you.",
    "what can you do": "I can answer simple questions and provide information.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what is the capital of India": "The capital of India is New Delhi.",
    "who is the prime minister of India": "As of 2023, the Prime Minister is Narendra Modi.",
    "what is the national animal of India": "The Bengal Tiger is the national animal of India.",
    "what is the national flower of India": "The Lotus is the national flower of India.",
    "what is the national bird of India": "The Indian Peafowl, also known as the Peacock, is the national bird.",
    "what is the national sport of India": "Field Hockey is considered the national sport of India.",
    "what is the national fruit of India": "The Mango is the national fruit of India.",
    "what is the national language of India": "India does not have a national language, but Hindi and English are official languages.",
    "what is the currency of India": "The currency of India is the Indian Rupee (INR).",
    "what is the population of India": "India has a population of over 1.3 billion people.",
    "what is the largest state in India": "Rajasthan is the largest state in India by area.",
    "what is the smallest state in India": "Goa is the smallest state in India by area.",
    "what is the highest mountain in India": "Kangchenjunga is the highest mountain in India.",
    "what is the longest river in India": "The Ganges is the longest river in India.",
    "what is the largest city in India": "Mumbai is the largest city in India by population.",
    "what is the national anthem of India": "The national anthem of India is 'Jana Gana Mana'.",
    "what is the national song of India": "The national song of India is 'Vande Mataram'.",
    "what is the national emblem of India": "The Lion Capital of Ashoka is the national emblem of India.",
    "what is the national tree of India": "The Banyan Tree is the national tree of India.",
    "what is the national river of India": "The Ganges is considered the national river of India.",
    "what is the national dish of India": "India does not have an official national dish, but Khichdi is often considered.",
    "what is the national festival of India": "Diwali is one of the major festivals celebrated across India.",
    "what is the national park of India": "Jim Corbett National Park is the oldest national park in India.",
    "what is the national monument of India": "The India Gate is a famous national monument in India.",
    "what is the national museum of India": "The National Museum in New Delhi is a major museum in India.",
    "what is the national library of India": "The National Library of India is located in Kolkata.",
    "what is the national university of India": "The University of Delhi is one of the prestigious universities in India.",
    "what is the national airline of India": "Air India is the national airline of India.",
    "what is the national railway of India": "Indian Railways is the national railway system of India.",
    "what is the national highway of India": "The Golden Quadrilateral is a major highway network in India.",
    "what is the national river of India": "The Ganges is considered the national river of India.",
    "what is the national mountain of India": "Kangchenjunga is the highest mountain in India.",
    "what is the national lake of India": "Wular Lake is one of the largest freshwater lakes in India.",
    "what is the national sea of India": "The Arabian Sea is on the western coast of India.",
    "what is the national ocean of India": "The Indian Ocean is named after India.",
    "what is the national forest of India": "Sundarbans is a famous mangrove forest in India.",
    "what is the national desert of India": "The Thar Desert is the largest desert in India.",
    "what is the national island of India": "The Andaman and Nicobar Islands are a group of islands in India.",
    "what is the national peninsula of India": "The Indian Peninsula is a major landform in India.",
    "what is the national gulf of India": "The Gulf of Kutch is a large gulf in India.",
    "what is the national bay of India": "The Bay of Bengal is a large bay on the eastern coast of India.",
    "why is the sky blue": "Because it reflects the ocean! Just kidding, it's due to Rayleigh scattering.",
    "can you dance": "I can try, but I might need some help with the moves!",
    "do you sleep": "I don't need sleep, but I do enjoy a good rest mode.",
    "can you cook": "I can suggest recipes, but cooking is not my strong suit!",
    "do you have a pet": "I don't have a pet, but I think a virtual cat would be fun!",
    "can you sing": "I can hum a tune, but I might be a bit off-key!",
    "default": "I'm sorry, I don't understand that."
}

@app.route("/")
def index():
    return render_template_string(open('index.html').read())

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message").lower()
    print(f"User input: {user_input}")  # Debugging line
    
    # Find a response
    response_text = responses.get(user_input, responses["default"])
    print(f"Response: {response_text}")  # Debugging line
    
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)