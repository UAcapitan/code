import re

# pattern_1 = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
# pattern_2 = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
pattern_3 = '[a-z]-[A-Z]-[0-9]'

user_input = input()

if (re.search(pattern_3, user_input)):
    print('Valid')
else:
    print('Not valid')