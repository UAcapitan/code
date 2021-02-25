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