from datetime import datetime
from math import pi, pow
from square import rectangle, triangle, circle
from random import randrange, randint
from copy import copy

# Разница целочисельных чисел с помощью сумирования
def subtracting_numbers(a_num,b_num):
    i = 0
    while True:
        if b_num + i == a_num:
            break
        i += 1
    return i

# Умножение целочисельных чисел с помощью сумирования
def multiplication_of_numbers(a_num,b_num):
    i = 0
    sum_numbers = 0
    while i < b_num:
        sum_numbers += a_num
        i += 1
    return sum_numbers

# Деление целочисельных чисел нацело с помощью сумирования
def division_of_numbers(a_num,b_num):
    i = 0
    while True:
        num = multiplication_of_numbers(b_num,i)
        if num == a_num:
            break
        i += 1
    
    return i

# Поменять значения переменных между собой без введения новой переменной
def changing_values(a_num,b_num):
    a_num = a_num + b_num
    b_num = a_num - b_num
    a_num = a_num - b_num
    return str(a_num) + ' ' + str(b_num)

# Поменять значения переменных между собой без введения новой переменной. 2 способ
def changing_values2(a_num,b_num):
    a_num, b_num = b_num, a_num
    return str(a_num) + ' ' + str(b_num)

# Функция генератора псевдослучайных чисел
def my_random_function():
    seconds = datetime.now().strftime("%S")
    random_number = str(int((((int(seconds) / 3) * 1.5) - 5) * 3))[-1]
    return random_number

# Регистрация и вывод списка зарегестрированых
dict_users = {}

def add_user_in_dict(user,password):
    dict_users.setdefault(user,password)

def read_dict_users(dict_users):
    for key, value in dict_users.items():
        print('User ' + key + ' have password ' + value)

for i in range(11):
    pass
    # name = input("Name: ")
    # password = input("Password: ")
    # add_user_in_dict(name,password)
    # read_dict_users(dict_users)

# Данные и их типы. Задания
# 1.
var_int = 10
var_float = 8.4
var_str = "No"

# 2.
var_big = var_int * 3.5

# 3.
var_float -= 1

# 4.
var_int / var_float
var_big / var_float

# 5.
var_str = "No" * 2 + "Yes" * 3

# 6.
# print(var_int)
# print(var_float)
# print(var_str)
# print(var_big)

# Ввод и вывод данных
# 1.

# name = input("What is your name?")
# age = input("How old are you?")
# city = input("Where are you live?")

# print("This is " + name )
# print("It is " + age)
# print("(S)he live in " + city)

# 2.

# num = input("4 * 100 - 54 = ")
# print('True = 346. User = ' + num)

# 3.
# n1 = int(input("Number 1: "))
# n2 = int(input("Number 2: "))
# n3 = int(input("Number 3: "))
# n4 = int(input("Number 4: "))

# n1_n2 = n1 + n2
# n3_n4 = n3 + n4
# sum_nums = n1_n2 / n3_n4
# print("%.2f" % sum_nums)

# Логические выражения и операторы
# 1.
# n = 2
# m = 3

# 2.
# print(n <= 2 and m == 3)
# print(n > 4 and m == 3)

# 3.
# print(n < 2 or m == 3)
# print(n > 4 or m < 3)

# 4.
# str1 = "Hi"
# str2 = "World"

# print(str1 < str2)
# print(str1 > str2)

# 5.
# n1 = input("Number 1: ")
# n2 = input("Number 2: ")

# if n1 > n2:
#     print(True)
# else:
#     print(False)

# Полносстью перевернуть матрицу
def reverse_matrix(array):
    for i in range(len(array)):
        array[i].reverse()
    array.reverse()
    return array

matrix_for_text = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# reverse_matrix_for_test = reverse_matrix(matrix_for_text)

# for i in reverse_matrix_for_test:
#     print(i)

# Ветвление. Условный оператор

# 1.
# n = input("Введите что-то: ")
# if n != '':
#     print('ОК')

# 2.
# n = int(input("Введите число: "))
# if n > 0:
#     print(1)
# else:
#     print(-1)

# Ошибки и исключения. Обработка исключений
# 1.

# n1 = input("Number 1: ")
# n2 = input("Number 2: ")

# try:
#     n1 = int(n1)
#     n2 = int(n2)
#     sum_nums = n1 + n2
# except:
#     sum_nums = n1 + n2

# print(sum_nums)

# Множественное ветвление: if-elif-else

# 1.
# old = int(input('Ваш возраст: '))

# print('Рекомендовано:', end=' ')

# if 3 <= old < 6:
#     print('Заяц в лабиринте')
# elif 6 <= old < 12:
#     print('Марсианин')
# elif 12 <= old < 16:
#     print('Загадочный остров')
# elif 16 <= old:
#     print('Поток сознания')
# else:
#     print('---')

# 2.
# try:
#     old = int(input('Ваш возраст: '))

#     print('Рекомендовано:', end=' ')

#     if 3 <= old < 6:
#         print('Заяц в лабиринте')
#     elif 6 <= old < 12:
#         print('Марсианин')
#     elif 12 <= old < 16:
#         print('Загадочный остров')
#     elif 16 <= old:
#         print('Поток сознания')
#     else:
#         print('---')
# except ValueError:
#     print('Введите целое число!')

# 3.
# n = int(input('Введите число: '))

# if n > 0:
#     print(1)
# elif n < 0:
#     print(-1)
# else:
#     print(0)

# Циклы в программировании. Цикл while

# 1.
# total = 100

# while total > 0:
#     n = int(input())
#     if total - n < 0:
#         print('Недопустимая операция')
#         quit()
#     total = total - n

# 2.
# i = 0
# while i <= 20:
#     print(2**i)
#     i += 1

# Проверка форматирования с помощью %7d
# print("%7d" % 2**i)

# Функции в программировании

# 1.
def test(n):
    if n > 0:
        positive()
    elif n < 0:
        negative()

def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

# test(1)
# test(-1)

# Локальные и глобальные переменные

# 1.
def cylinder(r,h):

    cylinder_result = 2 * pi * r * h

    def circle(r):
        return pi * (r**2)

    circle_result = circle(r)

    question = input('Найти полную площадь?')

    if question == 'y':
        return cylinder_result + circle_result
    else:
        return cylinder_result

# print(cylinder(10,5))    

# Возврат значений из функции. Оператор return

# 1.
def string_concatenation():
    str1 = input('Введите первое слово: ')
    str2 = input('Введите второе слово: ')
    result = str1 + str2
    return result

# print(string_concatenation())

# 2.
def multiplication_of_many_numbers():
    sum = 1
    while True:
        n = int(input('Введите число: '))
        if n == 0:
            break
        else:
            sum *= n
    return sum

# print(multiplication_of_many_numbers())

# Параметры и аргументы функции

# 1.
def get_input():
    return input()

# 2.
def test_input(value):
    try:
        value = int(value)
        return True
    except:
        return False

# 3.
def str_to_int(value):
    return int(value)

# 4. 
def print_int(value):
    print(value)

# Программа к заданию
# value = get_input()
# if test_input(value):
#     print_int(str_to_int(value))

# Встроенные функции

# 1.
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     print(chr(n))

# 2.
# str_input = input('Введите текст: ')
# len_str = len(str_input)
# if len_str > 10:
#     print('Warning')
# else:
#     i = len_str
#     while i < 10:
#         str_input += '*'
#         i += 1
#     print(str_input)

# 3.
# array_nums = []

# while True:
#     array_nums.append(float(input()))
#     if len(array_nums) == 6:
#         break

# min_num = array_nums[0]
# max_num = array_nums[0]


# for i in array_nums:
#     if i < min_num:
#         min_num = i
#     if i > max_num:
#         max_num = i

# print("Min: %.2f" % min_num)
# print("Max: %.2f" % max_num)

# Модули

# 1.
# from math import pi, pow
# def rectangle(a,b):
#     return round(a*b,2)

# def triangle(a,h):
#     return round(0.5*a*h,2)

# def circle(r):
#     return round(pi * pow(r,2),2)

# select_function = input()

# if select_function == 'r':
#     print(rectangle(10,2))
# elif select_function == 't':
#     print(triangle(10,2))
# elif select_function == 'c':
#     print(circle(10))

# Генератор псевдослучайных чисел - random

# 1.
# print(randrange(6,12))
# print(randrange(5,100,5))

# 2.
# n1 = int(input())
# n2 = int(input())
# select_type = input()

# if select_type == 'i':
#     print(int(randrange(n1,n2)))
# elif select_type == 'f':
#     print(float(randrange(n1,n2)))

# Списки

# 1.
# array_news = []
# while len(array_news) < 8:
#     array_news.append(int(input()))

# print('Sum: ',sum(array_news))
# print('Max: ',max(array_news))
# print('Min: ',min(array_news))

# 2.
# array_random_nums = []
# while len(array_random_nums) < 100:
#     array_random_nums.append(float(randint(0,100)))

# def output_string(array):
#     i = 0
#     j = 0
#     while int(str(j) + str(i))<100:
#         print(array[int(str(j) + str(i))], end=' ')
#         i += 1
#         if i == 10:
#             print()
#             i = 0
#             j += 1

# output_string(array_random_nums)

# array_random_nums.sort()

# print()
# print()
# print()

# output_string(array_random_nums)

# Цикл for

# 1.
# array_nums = []
# for i in range(10):
#     array_nums.append(randint(0,100))

# print(array_nums)

# 2.
# array_nums = list(range(0,100,17))
# print(array_nums)

# 3.
# array_num = [-5,-4,-3,0,1,2,3]
# pos_nums = 0
# neg_nums = 0
# for i in array_num:
#     if i > 0:
#         pos_nums += 1
#     elif i < 0:
#         neg_nums += 1

# print('Positive numbers:',pos_nums)
# print('Negative numbers:',neg_nums)

# 4.
# array_text = []
# array_len_text = []
# for i in range(5):
#     array_text.append(input())
#     array_len_text.append(len(array_text[i]))

# print('Text array:', array_text)
# print('Text len array:', array_len_text)

# Строки

# 1.
# text = input('Введите текст: ')
# text_lower = 0
# text_upper = 0
# for i in text:
#     if i.islower():
#         text_lower += 1
#     elif i.isupper():
#         text_upper += 1

# if text_lower > text_upper or text_lower == text_upper:
#     print(text.lower())
# elif text_lower < text_upper:
#     print(text.upper())

# 2.
# while True:
#     n1 = input()
#     n2 = input()

#     if n1.isdigit() and n2.isdigit():
#         print(int(n1)+int(n2))
#     else:
#         continue

# Кортежи

# 1.
# array_nums = (1,2,3)
# print(array_nums)
# array_nums2 = copy(array_nums)
# print(array_nums2)
# array_nums3 = array_nums[0:3]
# print(array_nums3)

# array_nums2 = ()
# array_nums3 = ()

# print(array_nums2)
# print(array_nums3)
# print(array_nums)

# 3.
def filling_a_tuple_with_numbers(a,b):
    tuple_nums = []
    for i in range(0,10):
        tuple_nums.append(randint(a,b))

    return tuple(tuple_nums)

# tuple1 = filling_a_tuple_with_numbers(0,5)
# tuple2 = filling_a_tuple_with_numbers(-5,0)

# print(tuple1)
# print(tuple2)

# tuple3 = tuple1 + tuple2

# print(tuple3.count(0))

# Словари

# 1.
# school = {
#     '1a':20,
#     '1b':19,
#     '2b':23,
#     '6a':30,
#     '7c':19
# }

# for i in school:
#     print(i, end=' ')

# print()

# for i in school:
#     print(school[i], end=' ')

# print()
# print()

# school['1a'] = 23

# for i in school:
#     print(i, end=' ')

# print()

# for i in school:
#     print(school[i], end=' ')

# print()
# print()

# school.setdefault('8a', 25)

# for i in school:
#     print(i, end=' ')

# print()

# for i in school:
#     print(school[i], end=' ')

# print()
# print()

# del school['2b']

# for i in school:
#     print(i, end=' ')

# print()

# for i in school:
#     print(school[i], end=' ')

# print()
# print()

# 2.
# dict_items = {
#     1:'a',
#     2:'b',
#     3:'c'
# }

# def change_the_key_and_value_in_the_dict(dict_items):
#     new_dict_items = {}
#     for key,value in dict_items:
#         new_dict_items.setdefault(value, key)

#     return new_dict_items

# print(change_the_key_and_value_in_the_dict(dict_items.items()))

# Файлы

# 1.
# file_for_text = open('Desktop/EdMix/Python/data.txt','r')
# file_data_ru = open('Desktop/EdMix/Python/data_ru.txt','w')
# nums = {
#     'zero':'ноль',
#     'one':'один',
#     'two':'два',
#     'three':'три',
#     'four':'четыре',
#     'five':'пять',
#     'six':'шесть',
#     'seven':'семь',
#     'eight':'восемь',
#     'nine':'девять'
# }
# for i in file_for_text:
#     if i != '':
#         file_data_ru.write(nums[i[:-1]] + '\n')
# file_for_text.close()
# file_data_ru.close()

# 2.
# file_numbers = open('Desktop/EdMix/Python/nums.txt','r')
# sum = 0
# for i in file_numbers:
#     sum += int(i)

# print(sum)

# Генераторы списков

# 1.
# s1 = 'abcd'
# s2 = '01'
# text_array = []
# for i in s1:
#     for j in s2:
#         text_array.append(i + j)

# print(text_array)

# a = [1,2,3,4,5,6,7,8,9,10]
# new_a = []
# for i in a:
#     if i % 2 == 0:
#         new_a.append(i)

# print(new_a)

# a = [1,2,3]
# b = [4,5,6]
# new_array = []
# for i in a:
#     for j in b:
#         if i * j <= 10:
#             new_array.append((i,j))

# print(new_array)

# 2.
# array1 = [input() for i in range(5)]

# array2 = [i for i in array1 if i.isdigit()]

# print(array1)
# print(array2)

# Матрицы

# 1.
# random_matrix = []
# for i in range(4):
#     random_array = []
#     for j in range(4):
#         random_array.append(randint(-10,10))
#     random_matrix.append(random_array)

# for i in random_matrix:
#     for j in i:
#         if j >= 0:
#             print(j, end=' ')
#         elif j < 0:
#             print('-', end=' ')
#     print()

# 2.
# random_matrix = []
# for i in range(4):
#     random_array = []
#     for j in range(4):
#         random_array.append(randint(-10,10))
#     random_matrix.append(random_array)

# array_sum = []

# for i in random_matrix:
#     array_sum.append(sum(i))

# print(array_sum)

# Множества

# 1.
# set_tags = set()
# while True:
#     text = input()
#     if text == 'stop':
#         break
#     if text in set_tags:
#         print('Has already')
#         continue
#     set_tags.add(text)
#     print(set_tags)

# Особенности работы операторов and и or

# 1.
# print(input() or 'User')

# 2.
# print(input() in [1,2,3] or quit())

# Lambda-выражения

# 1.
# array_list = [
#     (lambda i,j:i+j),
#     (lambda i,j:i-j),
#     (lambda i,j:i*j),
#     (lambda i,j:i/j)
#     ]
# print(array_list[1](1,4))

# 2.
# list_text = ['text','user','file']
# list_text.sort(key=lambda i: i[-1])
# list_text.sort(key=lambda i: len(i))

# print(list_text)