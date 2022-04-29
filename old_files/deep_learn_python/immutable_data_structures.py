my_tuple = (1,2,3)

print(my_tuple)
print(my_tuple[2])

try:
    my_tuple[1] = 3
except:
    pass

print(my_tuple)

my_tuple = (1,2,3,[1,2,3])

print(my_tuple)

print(my_tuple[3])

try:
    my_tuple[3] = 4
except:
    pass

print(my_tuple)

my_tuple[3][1] = 0

print(my_tuple)

my_list = my_tuple[3]

my_list[0] = 0

print(my_list)

print(my_tuple)

print(id(my_tuple))

try:
    my_tuple += (1,2,3)
except:
    pass

print(my_tuple)

print(id(my_tuple))

numbers = (1, 2, 3)
numbers2 = (1, 2, 3)
print(id(numbers))
print(id(numbers2))
print(numbers == numbers2)
print(numbers is numbers2)
print(numbers is numbers)
print(type(numbers) == type(numbers2))