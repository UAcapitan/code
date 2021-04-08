from random import randint
from time import sleep
from os import system
import hmac
import hashlib
import binascii
import secrets

# maketrans() и translate() - методы для замены символов 

def encode(string):
    return string.translate(string.maketrans('aeiou', '12345'))

def decode(string):
    return string.translate(string.maketrans('12345', 'aeiou'))

# print(encode('text'))
# print(decode('t2xt'))

# split() - метод для разбиения строки

def text_split(text):
    return ' '.join(text.split())

# print(text_split('  text     text '))

# strip() - удаление первые и последние символы, что подходят под условие
def strip_for_text(text):
    return text.strip('_')

# print(strip_for_text('_Text_'))
# print(strip_for_text('___Text_'))
# print(strip_for_text('_Text'))

# XOR
# key = 22
# n = int(input())
# print(n)
# n1 = n ^ key
# print(n1)
# n2 = n1 ^ key
# print(n2)

# Шифрование с помощью XOR

# class Encryption:
#     def __init__(self, key):
#         self.__key = key
#         self.num = 0
#     def enc(self,num):
#         return num ^ self.__key
#     def de_enc(self, num):
#         return num ^ self.__key

# enc_num = Encryption(22)
# print(enc_num.enc(155))
# print(enc_num.de_enc(141))

# Password generator

def password_generator(length):
    password = ''
    for i in range(length):
        n = randint(1,3)
        if n == 1:
            password += chr(randint(48,57))
        elif n == 2:
            password += chr(randint(65,90))
        else:
            password += chr(randint(97,122))
    return password

# print(password_generator(8))

# Список рандомных чисел

# list_rand = [randint(1,10) for i in range(10)]

# Вывод текста как ввод с клавиатуры

def output_text_keyboard(text):
    text_list = list(text)
    new_text_list = []
    for i in text_list:
        new_text_list.append(i)
        print(''.join(new_text_list))
        sleep(0.3)
        system('cls')

# output_text_keyboard('Hi, world, i am programmer and i write code')

# Number to time
def number_to_time(num: int) -> str:
    hours = num // 3600
    num -= hours * 3600
    minutes = num // 60
    seconds = num % 60
    list_time = [hours, minutes, seconds]
    list_time_new = [str(i) if i >= 10 else '0'+str(i) for i in list_time]
    return ':'.join(list_time_new)

# print(number_to_time(7011))

def delete_odd_numbers(l:list) -> list:
    return [i for i in l if i % 2 == 1]

# print(delete_odd_numbers([1,2,3,4,5]))

# Подсчёт количества строк

def amount_rows_in_file(address):
    count = 0
    with open(address, 'r') as file:
        for i in file:
            count += 1
    return count

# print(amount_rows_in_file('../../src/text/text_string.txt'))

# Пересоздание файла пустым

def create_empty_file(name_file):
    with open(name_file, 'w') as file:
        file.write('')
    return True

# print(create_empty_file('../../src/text/text.txt'))

# Создать ключ и hmac
class HmacCreate:
    @staticmethod
    def create_key():
        return secrets.token_bytes(16)

    @staticmethod
    def create_hmac(text_user: str):
        text_user = text_user.encode()
        return hmac.new(HmacCreate.create_key(), text_user, hashlib.sha256).hexdigest().upper()

# print(HmacCreate.create_hmac('text'))