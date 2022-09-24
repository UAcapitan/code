
from array import array
from collections import namedtuple


symbols = "$%*#&^!"

codes1 = []
for symbol in symbols:
    codes1.append(ord(symbol))

codes2 = [ord(symbol) for symbol in symbols]

codes3 = (ord(symbol) for symbol in symbols)

# print(codes1 == codes2)
# print(codes2 == codes3)

# for i in codes3:
    # print(i)


# Iterator vs generator
colors = ['white', 'black']
sizes = ['S', 'M', "L"]

t_shirts = [(color, size) for color in colors for size in sizes]
t_shirts_gen = ((color, size) for color in colors for size in sizes)

# print(t_shirts)

# for t_shirt in t_shirts_gen:
#     print(t_shirt)


# Tuple comprehension
tuple_symbols = tuple(ord(symbol) for symbol in symbols)
# print(tuple_symbols)
# print(tuple_symbols == codes3)


# Array
array_symbols = array('I', [ord(symbol) for symbol in symbols])
array_symbols.append(1)
# print(array_symbols)


# Working with tuple
numbers = tuple(range(1,6))

a, b, *rest = numbers
# print(a, b, rest)
a, *rest, b = numbers
# print(a, rest, b)
*rest, a, b = numbers
# print(rest, a, b)


# Namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 129.691667))
print(tokyo)