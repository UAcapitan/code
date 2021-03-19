from random import randint

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

list_rand = [randint(1,10) for i in range(10)]
