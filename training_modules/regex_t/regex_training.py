import re

# pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
# pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
# pattern = '[a-z]-[A-Z]-[0-9]'
# pattern = '[\d]{10}-[abc]v1'
# pattern = '\t\s\t\s\w'
# pattern = '[^a]\d\t\w'
# pattern = '.{3}-\w'
# pattern = '^[a-zA-Z0-9]{5}$'
pattern = '(good|bad|nice) man'

def search_pattern(p):
    if (re.search(p, input())):
        print('Valid')
    else:
        print('Not valid')

# search_pattern(pattern)

text = '123 123 123 ed@gmail.com ' \
    '123textuser user123 who am I' \
    'I don`t know' \
    'Hello, friend main@gmail.com' \
    ' c.at@poshta.ua 223 good_day'

pattern = '[a-zA-Z.]+@\w+\.\w{2,5}'
# pattern = '\d\d\d'

def find_text(p, t):
    print(re.findall(p, t))

find_text(pattern, text)

