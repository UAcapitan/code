from random import randint

# Создание классов и объектов

# 1.
# class warrior:
#     health = 100
#     def decrease_health(self):
#         self.health -= 20

# warrior1 = warrior()
# warrior2 = warrior()

# while True:
#     if warrior1.health == 0:
#         break
#     if warrior2.health == 0:
#         break

#     random_number = randint(1,2)
#     if random_number == 1:
#         warrior2.decrease_health()
#         print('Warrior 1 > Warrior 2',warrior2.health)
#     elif random_number == 2:
#         warrior1.decrease_health()
#         print('Warrior 2 > Warrior 1',warrior1.health)

# if warrior1.health > warrior2.health:
#     print('Warrior 1 win')
# else:
#     print('Warrior 2 win')

# Конструктор класса - метод __init__()

# 1. 2. 3. 4.
# class Person:
#     def __init__(self, name, full_name, job_level = 1):
#         self.name = name
#         self.full_name = full_name
#         self.job_level = job_level
#     def get_info_about_user(self):
#         return self.name + ' ' + self.full_name + ' Job Level: ' + str(self.job_level)
#     def __del__(self):
#         print('До свидания, мистер ', self.name, self.full_name)

# Andrey = Person('Andrey','Igorev',2)
# Ina = Person('Ina','Igorevna',3)
# Igor = Person('Igor','Igorev')

# print(Andrey.get_info_about_user())
# print(Ina.get_info_about_user())
# print(Igor.get_info_about_user())

# del Igor

# input()

# Наследование

# 1.
# class Person:
#     count = 0
#     def __init__(self,team):
#         self.id_original = Person.count
#         Person.count += 1
#         self.team = team

# class soldier(Person):
#     def __init__(self,team):
#         Person.__init__(self,team)
#         self.my_hero = None
#     def going_to_the_hero(self, hero):
#         self.my_hero = hero.id_original

# class hero(Person):
#     def __init__(self, team):
#         Person.__init__(self,team)
#         self.level = 1
#     def up_level(self):
#         self.level += 1

# hero1 = hero(1)
# hero2 = hero(2)

# army1 = []
# army2 = []

# for i in range(10):
#     random_number = randint(1,2)
#     if random_number == 1:
#         army1.append(soldier(random_number))
#     elif random_number == 2:
#         army2.append(soldier(random_number))

# print(len(army1), len(army2))

# if len(army1) > len(army2):
#     hero1.up_level()
# elif len(army2) > len(army1):
#     hero2.up_level()

# army1[0].going_to_the_hero(hero1)

# print('Hero1: ', hero1.id_original)
# print('Soldier : ', army1[0].id_original)