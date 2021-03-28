from random import randint
from math import ceil, pi
from abc import ABC, abstractclassmethod
from interface import implements, Interface
from requests import post
# from my_modules import room, win_door


# Создание классов и объектов

# 1.
# class Warrior:
#     health = 100
#     def decrease_health(self):
#         self.health -= 20

# warrior1 = Warrior()
# warrior2 = Warrior()

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

# class Soldier(Person):
#     def __init__(self,team):
#         Person.__init__(self,team)
#         self.my_hero = None
#     def going_to_the_hero(self, hero):
#         self.my_hero = hero.id_original

# class Hero(Person):
#     def __init__(self, team):
#         Person.__init__(self,team)
#         self.level = 1
#     def up_level(self):
#         self.level += 1

# hero1 = Hero(1)
# hero2 = Hero(2)

# army1 = []
# army2 = []

# for i in range(10):
#     random_number = randint(1,2)
#     if random_number == 1:
#         army1.append(Soldier(random_number))
#     elif random_number == 2:
#         army2.append(Soldier(random_number))

# print(len(army1), len(army2))

# if len(army1) > len(army2):
#     hero1.up_level()
# elif len(army2) > len(army1):
#     hero2.up_level()

# army1[0].going_to_the_hero(hero1)

# print('Hero1: ', hero1.id_original)
# print('Soldier : ', army1[0].id_original)

# Полиморфизм

# class Number_sum:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __add__(self,other):
#         print(other.a,other.b)
#         return Number_sum(other.a,other.b)

# my_number = Number_sum(10,20)
# other_number = Number_sum(30,40)

# print(other_number + my_number)
# print(my_number + other_number)
# print(my_number + other_number + my_number)

# Инкапсуляция

# class User_id:
#     __id = 0
#     def __init__(self):
#         User_id.__id += 1
#     @staticmethod
#     def get_id():
#         return(User_id.__id)
#     def __get_dict(self):
#         return(User_id.__dict__)
#     def __setattr__(self,attr,value):
#         if attr == '__id':
#             self.__dict__[attr] = value
#         else:
#             raise AttributeError

#     print(__get_dict)

# print(User_id.get_id())
# user1 = User_id()
# print(User_id.get_id())
# user1.id2 = 0

# Композиция

# class Win_door:
#     def __init__(self,x,y):
#         self.square = x * y

# class Room:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.wd = []
#         self.list_weight = []
#     def add_win_door(self,w,h):
#         self.wd.append(Win_door(w,h))
#     def work_surface(self):
#         new_square = self.square_for_use
#         for i in self.wd:
#             new_square -= i.square
#         return new_square
#     def change_size(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.save_weight()
#     def save_weight(self):
#         self.list_weight.append([self.x,self.y])
#     def calculate_squere(self):
#         self.square = 2*self.z*(self.x+self.y)
#         self.square_for_use = self.square
#     def number_of_rolls(self,x,y):
#         return ceil(self.square_for_use / (x*y))

# r1 = Room(6,3,2.7)
# r1.calculate_squere()
# print(r1.square_for_use)
# r1.add_win_door(1,1)
# r1.add_win_door(1,1)
# r1.add_win_door(1,2)
# print(r1.work_surface())
# r1.save_weight()
# r1.change_size(2,3,4)
# print(r1.square_for_use)
# r1.save_weight()
# print(r1.list_weight)
# print(r1.number_of_rolls(2,2))

# Перегрузка операторов

# class Snow:
#     def __init__(self,s):
#         self.snowflakes = s
#     def __add__(self,b):
#         self.snowflakes += b
#         return self.snowflakes
#     def __sub__(self,b):
#         self.snowflakes -= b
#         return self.snowflakes
#     def __mul__(self,b):
#         self.snowflakes *= b
#         return self.snowflakes
#     def __truediv__(self,b):
#         self.snowflakes /= b
#         self.snowflakes = int(self.snowflakes)
#         return self.snowflakes
#     def make_snow(self):
#         text_snow = '*****\n' * int(self.snowflakes / 5) + '*' * (self.snowflakes - (int(self.snowflakes / 5) * 5))
#         return text_snow.strip('\n')
#     def __call__(self,new_value):
#         self.snowflakes = new_value

# snow1 = Snow(10)
# print(snow1.snowflakes)
# print(snow1 + 2)
# print(snow1 - 10)
# print(snow1 * 2)
# print(snow1 / 10)
# snow2 = Snow(10)
# snow2(9)
# print(snow2.make_snow())

# Модули и пакеты

# r1 = room.Room(3,4,3)
# r1.calculate_squere()
# print(r1.square_for_use)
# r1.add_win_door(1,1)
# r1.add_win_door(1,1)
# r1.add_win_door(1,2)
# print(r1.work_surface())
# r1.save_weight()
# r1.change_size(2,3,4)
# print(r1.square_for_use)
# r1.save_weight()
# print(r1.list_weight)
# print(r1.number_of_rolls(2,2))

# Документирование кода

# Тестирование работы документирования
# class Test:
#     """Hello"""
#     def __init__(self):
#         self.n = 1

# help(Test)

# Практичское задание
# help(room.Room)
# print(win_door.Win_door.__doc__)
# print(room.Room.add_win_door.__doc__)
# print(room.Room.change_size.__doc__)
# print(room.Room.number_of_rolls.__doc__)

# Пример объектно-ориентированной программы на Python

# class Data:
#     def __init__(self, *info):
#         self.info = list(info)
#     def __getitem__(self,i):
#         return self.info[i]

# class Teacher:
#     def __init__(self):
#         self.work = 0
#     def teach(self, info, *pupil):
#         for i in pupil:
#             i.take(info)
#             self.work += 1

# class Pupil:
#     def __init__(self):
#         self.knowledge = []
#     def take(self, info):
#         self.knowledge.append(info)
#     def forget(self):
#         n_random = randint(0, len(self.knowledge) - 1)
#         del self.knowledge[n_random]

# lesson = Data('class','object','inheritance','polymorphism','encapsulation')
# mar_Ivanna = Teacher()
# vasy = Pupil()
# pety = Pupil()
# mar_Ivanna.teach(lesson[2], vasy, pety)
# mar_Ivanna.teach(lesson[0], pety)
# print(vasy.knowledge)
# print(pety.knowledge)
# vasy.take(lesson[1])
# print(vasy.knowledge)
# vasy.forget()
# print(vasy.knowledge)

# Статические методы

# class Cylinder:
#     @staticmethod
#     def make_area(d,h):
#         circle = pi * d ** 2 / 4
#         side = pi * d * h
#         return round(circle * 2 + side, 2)

#     def __init__(self, diameter, high):
#         self.__dict__['dia'] = diameter
#         self.__dict__['h'] = high
#         self.__dict__['area'] = self.make_area(diameter, high)

#     def __setattr__(self,attr,value):
#         if attr == 'dia':
#             self.__dict__['dia'] = value
#             self.__dict__['area'] = self.make_area(self.dia, self.h)
#         elif attr == 'h':
#             self.__dict__['h'] = value
#             self.__dict__['area'] = self.make_area(self.dia, self.h)
#         elif attr == 'area':
#             print('This field cannot be changed')

# a = Cylinder(1,2)
# print(a.__dict__['area'])
# print(a.make_area(2,2))
# print(a.__dict__['area'])
# a.dia = 50
# print(a.__dict__['area'])
# a.h = 10
# print(a.__dict__['area'])
# a.area = 100

# Итераторы

# Пример
# class Letters:
#     def __init__(self, string):
#         self.letters = []
#         for i in string:
#             self.letters.append(i)
#     def __iter__(self):
#         return Letters_iterator(self.letters)

# class Letters_iterator:
#     def __init__(self, letters):
#         self.letters = letters
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.letters == []:
#             raise StopIteration
#         item = self.letters[0]
#         del self.letters[0]
#         return item

# kit = Letters('aeoui')
# print(kit.letters)

# for i in kit:
#     print(i)

# Задание
# class Random_list:
#     def __init__(self, j, x, y):
#         self.random_list = []
#         for i in range(j):
#             self.random_list.append(randint(x,y))
#     def print_random_list(self):
#         print(self.random_list)
#     def __next__(self):
#         if self.random_list == []:
#             raise StopIteration
#         item = self.random_list[0]
#         del self.random_list[0]
#         return item
#     def __iter__(self):
#         return self
    
    
# l = Random_list(5,0,5)
# l.print_random_list()
# for i in l:
#     print(i)

# Генераторы

# class Generator:
#     def __init__(self, j, x, y):
#         self.j = j
#         self.x = x
#         self.y = y
#     def generator_random_list(self):
#         self.list_random = (randint(self.x, self.y) for i in range(self.j))
#     def print_generator_random_list(self):
#         for i in self.list_random:
#             print(i)

# l = Generator(5,0,5)
# l.generator_random_list()
# l.print_generator_random_list()

# Класс для обработки имени

# class Name_proccesing:
#     def __init__(self, name='User',n=1,j=1):
#         self.name = name
#         self.__n = n
#         self.__j = j
#         self.name_num = self.name_in_num()
#         self.name_enc = self.name_in_enc()
#     def name_in_num(self):
#         name_num = []
#         for i in self.name:
#             name_num.append(str(ord(i)) + ' ')
#         return ''.join(name_num).strip()
#     def num_in_name(self):
#         num_name = []
#         num_1 = self.name_num.split()
#         for i in num_1:
#             num_name.append(chr(int(i)))
#         return ''.join(num_name)
#     def name_in_enc(self):
#         name_enc = []
#         for i in self.name:
#             if self.__j >= 0:
#                 name_enc.append(chr(ord(i) + int(self.__n)))
#             else:
#                 name_enc.append(chr(ord(i) - int(self.__n))) 
#         return ''.join(name_enc)
#     def enc_in_enc(self):
#         enc_name = []
#         for i in self.name_enc:
#             if self.__j >= 0:
#                 enc_name.append(chr(ord(i) - int(self.__n)))
#             else:
#                 enc_name.append(chr(ord(i) + int(self.__n))) 
#         return ''.join(enc_name)

# name_user = Name_proccesing('Vasy')
# print(name_user.name_num)
# print(name_user.num_in_name())
# print(name_user.name_enc)
# print(name_user.enc_in_enc())

# Абстрактный класс

class ChessPiece(ABC):
    def draw(self):
        print('Drew a chess piece')

    @abstractclassmethod
    def move(self):
        pass

class Queen(ChessPiece):
    def move(self):
        print('Moved Queen to e2e4')

# queen = Queen()
# queen.draw()
# queen.move()

# Абстрактный метод

class Basic(ABC):
    @abstractclassmethod
    def hello(self):
        print('Hello from Basic class')

class Advanced(Basic):
    def hello(self):
        super().hello()
        print('Enriched functionality')

# a = Advanced()
# a.hello()

# Интерфейс

class My_Interface(Interface):
    def method_1(self, x):
        pass

    def method_2(self, x, y):
        pass

class My_Class(implements(My_Interface)):
    def method_1(self, x):
        return x * 2

    def method_2(self, x, y):
        return x + y

# a = My_Class()
# print(a.method_1(10))
# print(a.method_2(10,20))

# Абстрактный класс. Тренировка 1
class Item(ABC):
    def __init__(self):
        self.name = input('Item name: ')
    
    def name_item(self):
        return self.name
    
    def rename_item(self):
        self.name = input('Item new name: ')

    @abstractclassmethod
    def skills_item(self, name_skill='', power=0):
        self.name_skill = name_skill
        self.power = power

class Tools(Item):
    def skills_item(self):
        super().skills_item(input('Name skill: '),int(input('Power: ')))

class Cars(Item):
    def skills_item(self, speed, weight):
        self.speed = speed
        self.weight = weight

# tool = Tools()
# tool.skills_item()

# car = Cars()
# car.skills_item(200,1200)

# print(tool.name_skill, car.speed)

# Абстрактный класс. Тренировка 2

# pylint: disable=no-member
class Phone(ABC):

    def make_photo(self):
        '''Method for make photo. Method not work if phone haven`t camera'''
        if self.camera and len(self.photo) > 0:
            photo = self.photo[-1][:-1] + str(int(self.photo[-1][-1]) + 1)
            print(f'Make {photo}')
            self.photo.append(photo)
        elif self.camera and len(self.photo) == 0:
            self.photo.append('image_1')
            print('Make image_1')
        else:
            print('Your phone no have camera')

    def browser_go_in_site(self, url):
        '''Method for browsing'''
        site = post(url)
        if site.status_code == 200:
            print(site)
            self.browser_history.append(url)
        else:
            print('Sorry')

    def browser_open_history(self):
        '''Open history in phone browser'''
        print('-----------------\nBrowser history')
        if len(self.browser_history) > 0:
            for site in self.browser_history:
                print(site)
        else:
            print('No history')

        print('-----------------')
        input()

    def photos_open_list(self):
        '''Open list photos in phone'''
        print('-----------------\nPhotos list')
        if len(self.photo) > 0:
            for photo in self.photo:
                print(photo)
        else:
            print('No photos')

        print('-----------------')
        input()

    def create_user_account(self, name='', login='', password=''):
        if name != '' and login != '' and len(str(password)) >= 8:
            self.name = name
            self.login = login
            self.password = password
            print('\nAccount created')
        else:
            print('\nAccount not created')
        
        if len(str(password)) < 8:
            print('\nYou password little')

    def open_user_profile(self):
        if self.name != '':
            print(f'\nName: {self.name}')
            print(f'Login: {self.login}')
        else:
            print('\nYou don`t have account')

# Абстрактный класс. Тренировка 3
class Xphone(Phone):

    def __init__(self, camera):
        self.camera = camera
        self.photo = []
        self.browser_history = []
        self.name = ''

# Абстрактный класс. Тренировка 4
if __name__ == '__main__':
    xphone_1 = Xphone(camera=True)
    while True:
        print('\n1. Make photo\n2. Open photos\n3. Open site\n4. Open browser history\n5. Create account')
        print('6. Open user profile')
        command = input()
        if command == '1':
            xphone_1.make_photo()
        elif command == '2':
            xphone_1.photos_open_list()
        elif command == '3':
            xphone_1.browser_go_in_site(input('URL: '))
        elif command == '4':
            xphone_1.browser_open_history()
        elif command == '5':
            xphone_1.create_user_account(name=input('Name: '), login=input('Login: '), password=int(input('Password: ')))
        elif command == '6':
            xphone_1.open_user_profile()
        elif command == 'password':
            print(xphone_1.password)

        elif command == 'exit':
            break