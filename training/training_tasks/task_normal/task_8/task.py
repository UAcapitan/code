a = 5
b = 10

print(str(a) + ' - ' + str(b))

a,b = b,a

print(str(a) + ' - ' + str(b))

a = a + b
b = a - b
a = a - b

print(str(a) + ' - ' + str(b))