from app import pygame
import random


task_names = [
    'Max',
    'Leo',
    'Donald',
    'John',
    'Ira',
]

texts = [
    "Hello there, I am looking for some products for dinner.",
    "Hi. Do you have some products for me?",
    "I need some food immediately.",
    "What's up? I wanna it, really, so, please?",
    "Hi. I think about making a party. Also invite you.",
    f"Good day. Do you have something for my friend {random.choice(task_names)}.",
    "Good afternoon. I need to feed my family.",
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