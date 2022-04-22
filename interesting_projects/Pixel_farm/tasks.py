from app import pygame
import random


task_names = [
    'Max',
    'Leo',
    'Donald',
    'John',
    'Ira',
    'John Jr.',
    'Nikita',
    'Anna',
    'Angela',
    'Jack',
    'Teodor',
]

texts = []


def generate_task(self) -> list:
    return [
        random.choice(task_names),
    ]