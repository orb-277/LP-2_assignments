import re,random
rules= {
    'greeting':{
        'patterns':[r'hello',r'hi',r'hey'],
        'responses':['Hey babe']
    },
    'menu':{
        'patterns':[r'menu',r'options',r'choices'],
        'responses':['Hey babe heres menu']
    },
    'goodbye': {
        'patterns': [r'bye', r'goodbye', r'see you'],
        'responses': ['Thank you for choosing our food ordering service. Ab nikal BC yaha se', 'Goodbye!'],
    },
    'default': {
        'responses': ['Im sorry, I didnt understand that. Can you please rephrase?']
    }


}

def match_patterns(user_inp,patterns):
    for pattern in patterns:
        match = re.search(pattern,user_inp,re.IGNORECASE)
        if match:
            return True
    return False

def get_response(user_inp):
    for intent,data in rules.items():
        patterns = data.get('patterns')
        if patterns and match_patterns(user_inp,patterns):
            res = data.get('responses')
            return random.choice(res)
    return random.choice(rules['default']['responses'])

def chat():
    print("Chatbot: Hello! Welcome to our food ordering service.")
    while True:
        user_input = input("User: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        # Exit the loop if the user says goodbye
        if any(re.search(pattern, user_input) for pattern in rules['goodbye']['patterns']):
            break

# Start the chatbot
chat()