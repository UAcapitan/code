conversation_list_Max_1 = [
    'Hi! How are you? Are you a new farmer?',
    'I can help you for first time.',
    'You can destroy stones with special thing.',
    'But watch carefully at your energy',
    'But, anyway, our energy refill after some time.',
    ''
]

conversation_list_Leo_2 = [
    'Hello there! I am your neighbor! My name is Leo.',
    'I really like potato. May you give me some?',
    'You have not it. So, I can wait.',
    ''
]

conversation_list_Donald_3 = [
    'Hi, my name is Donald, but you can call me Donald.',
    'Leo said me about you. He said that your potato',
    'is not very bad. But I need some carrot for party.',
    'Yeah, carrot party, it is... it is... not strange.',
    'I really '
    ''
]

def generate_conversation(name, task):
    name = name
    if task == 1:
        return conversation_list_Max_1