f = open('text.txt', 'w')

f.write('Hello world!')

f.close()

with open('text.txt', 'w') as file:
    file.write('Hello world!\n')
    file.write('Test')

with open('text.txt') as file:
    print(file.read())

print()

a = {1,2,3,4,5}
b = {3,4,5}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

print()

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

print()

a = [1,2,3]
b = a
c = [1,2,3]

print(a == b)
print(a == c)

print()

print(a is b)
print(a is c)

print()