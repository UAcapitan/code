my_dict = {
    '1':'a',
    '2':'b',
    '3':'c'
}

print(my_dict)

my_dict.clear()
print(my_dict)

my_dict['1'] = 'a'
my_dict['2'] = 'b'
my_dict['3'] = 'c'
print(my_dict)

md = my_dict.copy()
print(md)

print(my_dict.fromkeys('1', 'a'))

print(my_dict.get('1'))

print(my_dict.items())

print(my_dict.keys())