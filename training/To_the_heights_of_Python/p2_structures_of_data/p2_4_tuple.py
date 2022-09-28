
numbers = tuple(range(1,6))

a, b, *rest = numbers
print(a, b, rest)
a, *rest, b = numbers
print(a, rest, b)
*rest, a, b = numbers
print(rest, a, b)
