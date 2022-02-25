def greeting(name: str) -> str:
    return f'Hello, {name}'

# print(greeting(3))
print(greeting('Ivan'))
# print(greeting(b'Max'))

def p() -> None:
    print(None)

# print(p())

def p2() -> None:
    return None

# print(p2())

def p3() -> None:
    1 + 2

# print(p3())

def hi(name: str, flag: bool) -> str:
    if flag:
        return f'Hi, {name}'
    return f'Hello, {name}'

print(hi('Max', True))