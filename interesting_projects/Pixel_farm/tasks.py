from app import pygame
import random


task_names = [
    'Max',
    'Leo',
    'Donald',
    'John',
    'Ira',
    # 'John Jr.',
    # 'Nikita',
    # 'Anna',
    # 'Angela',
    # 'Jack',
    # 'Teodor',
]

texts = [
    'Hello there, I am looking for some products for dinner.',
    'Hi. Do you have some products for me?',
    'I need some food immediately.',
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
    n = random.randint(1, 10)
    bonus = random.randint(0, 10)

    return [
        random.choice(task_names),
        random.choice(texts),
        [random.choice(items) for i in range(n)],
        n * 3 + level + bonus
    ]