text = input()

text_list = text.split()

big_word = ''

for i in text_list:
    if len(i) > len(big_word):
        big_word = i
    

text_dict = {}

for i in text_list:
    if i in text_dict.keys():
        text_dict[i] += 1
    else:
        text_dict.update({i: 1})

keys = []
values = []

for key in text_dict:
    keys.append(key)
    values.append(text_dict[key])


print(big_word)
print(keys[values.index(max(values))])