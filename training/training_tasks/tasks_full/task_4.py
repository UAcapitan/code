numbers_list = [1,2,3,4,5,6,7,8,9]

for i in enumerate(numbers_list):
    print(i[0], end=' ')

print()

for i in enumerate(numbers_list):
    print(i[1], end=' ')

print(end='\n\n')

test_string = 'Hello world! How are you?'

test_string_list = test_string.split()

print(test_string_list)

print()

new_test_string = '-'.join(test_string_list)

print(new_test_string)

print()

print(test_string.find('world'))

print()

print('{0}, {1}'.format(test_string_list[0],test_string_list[1]))

print(f'{test_string_list[0]}, {test_string_list[1]}')

print()

key_dict = {'one':1, 'two':2, 'ten':10}

for i in key_dict:
    print(i, end=' ')

print(end='\n\n')

for i, j in key_dict.items():
    print(i, j)

print()

key_list = ['one', 'two', 'ten']

new_key_dict = dict.fromkeys(key_list)

key_list_values = [1,2,10]

n = 0

for i in new_key_dict:
    new_key_dict[i] = key_list_values[n]
    n += 1

print(new_key_dict)

print()

print(new_key_dict.get('one'))

print()

new_key_dict.popitem()

print(new_key_dict)

print()

new_key_dict.pop('one')

print(new_key_dict)

print()

new_key_dict.setdefault('one', 1)

print(new_key_dict)

print()

new_key_dict.update({'ten':10})

print(new_key_dict)

print()