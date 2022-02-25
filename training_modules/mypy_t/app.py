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

# print(hi('Max', True))

def arg(*args: int, **kwargs: float) -> None:
    for i in args:
        print(i)
    for k, j in kwargs.items():
        print(f'{k} : {j}')

# print(arg(1,2,3,test=3.4))

def print_names(names: list[str]) -> None:
    for i in names:
        print(f'Hi, {i}')

print(print_names(['Max', 'Ivan', 'Ira']))
print(print_names([10,20,30]))