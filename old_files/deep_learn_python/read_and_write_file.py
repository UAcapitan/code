with open('foo.txt', 'r') as file:
    print(file.read())

with open('foo.txt', 'r') as file:
    print(file.readlines(1))
    print(file.readlines(1))
    print(file.readlines(1))

with open('foo.txt', 'r') as file:
    print(file.readlines())

with open('foo.txt', 'r') as file:
    for line in file.readlines():
        print(line, end='')

with open('foo.txt', 'r') as file:
    for line in file:
        print(line, end='')

with open('foo.txt', 'w') as file:
    file.write('Hello, world\nHow are you?')

with open('foo.txt', 'w') as file:
    l = ['Hello, world\n', 'How are you?']
    file.writelines(l)