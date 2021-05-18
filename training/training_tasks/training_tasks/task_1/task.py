import random

list_random = []
for i in range(3):
    list_random.append(random.randint(1,10))

print(list_random)

for i in range(len(list_random)):
    t = list_random[i]
    list_random[i] = '-'
    if t in list_random:
        print('False')
        exit()

print('True')