import random

l = [1,2,3]
print(random.choice(l)) # случайный выбор со списка

print(random.randint(1,10)) # случайное целое число

print(random.random()) # случайное число от 0 до 1

print(random.randrange(1,10,2)) # случайное число от 1 до 10 с шагом 2

l = [1,2,3,4,5,6,7,8,9]
print(random.choices(l)) # список со случайным выбором

random.shuffle(l)
print(l) # последовательность в случайном порядке

print(random.uniform(10, 20.22)) # случайное рациональное число
