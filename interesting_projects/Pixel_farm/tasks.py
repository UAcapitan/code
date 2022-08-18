import random

task_names = [
    'Max',
    'Leo',
    'Donald',
    'John',
    'Ira',
    'Mark',
    'Frank',
    'Mike',
    'Mia'
]

texts = [
    "Hello there, I am looking for some products for dinner.",
    "Hi. Do you have some products for me?",
    "I need some food immediately.",
    "What's up? I wanna it, really, so, please?",
    "Hi. I think about making a party. Also invite you.",
    f"Good day. Do you have something for my friend {random.choice(task_names)}.",
    "Good afternoon. I need to feed my family.",
    "I don't have enough time for speaking. Just give me things from this list.",
    "Excuse me. Could you give me these products?",
    "Mr. Farmer, hello! I am not sure what I want to eat today. So, give me something",
    f"Hi, hi! I am heaving the lunch with {random.choice(task_names)} tomorrow.",
    f"Hi! {random.choice(task_names)} is sick right now. {random.choice(task_names)} said to me that these products\
can help",
    "Hello, my friend. Did someone tell you that you are so lovely?",
    "Hi, my little friend. So...",
    f"Hello, {random.choice(task_names)}. Oh, ops, sorry. I think you are {random.choice(task_names)}. Oh, ops, again.",
    "Hi!",
]

items = [
    'wheat',
    'carrot',
    'potato',
    'grass',
    'onion',
    'cucumber',
]


def generate_task(level) -> dict:
    n = random.randint(1, 5)
    bonus = random.randint(0, 10)

    return {
        'name': random.choice(task_names),
        'text': random.choice(texts),
        'items': [random.choice(items) for i in range(n)],
        'price': n * 3 + level + bonus
    }