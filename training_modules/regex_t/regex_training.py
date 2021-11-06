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

user_input = input()

if (re.search(pattern, user_input)):
    print('Valid')
else:
    print('Not valid')