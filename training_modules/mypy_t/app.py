'''
    MyPy command start:
        mypy <name of file>
'''

from typing import *
from collections.abc import *

def greeting(name: str) -> str:
    return f'Hello, {name}'

# print(greeting(3))
# print(greeting('Ivan'))
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

# print(print_names(['Max', 'Ivan', 'Ira']))
# print(print_names([10,20,30]))

def print_list_of_names(names: List[str]) -> List[str]:
    return names

# print(['Max', 'John', 'Denis'])

def iter_only(names: Iterable[str]) -> list:
    return list(names)

# print(iter_only(iter(['Max', 'Ivan', 'Denis'])))

def str_and_none_only(name: Union[str, None]) -> Union[str, None]:
    return name

# print(str_and_none_only('Max'))
# print(str_and_none_only(None))

def str_optional(name: Optional[str] = None) -> str:
    if name is None:
        return 'Anonymous'
    return name

# print(str_optional('Max'))
# print(str_optional(None))

def condition_nums(iter_f: Iterable[float], n: int) -> list[float]:
    return [i for i in iter_f if i >= n]

# print(condition_nums(iter([1,2,3,4,5,6,7,8,9,10]), 5))

my_global_dict: dict[str, float] = {}
my_global_dict['test'] = 1
my_global_dict['test2'] = 1.1
# my_global_dict['test3'] = 'name'

x: str = ''
# x = 5
x = 'Text'

list_of_lists: List[List[int]] = []
list_of_lists = [[1,2,4]]
# list_of_lists = [[1,2,'test']]

x2 = chr(4)

a1: int
b1: float
c1: str

list1: list[int] = [1,2,3]
dict1: dict[str, int] = {
    '1': 1,
    '2': 2,
    '3': 3
}
set1: set[int] = {1,2,3}

x = print() #type: ignore
x3: Any = print()

a2 = [1]
b2 = cast(list[str], a2)
c2 = cast(list[int], a2)

b2.append('2')
# b2.append(2)
# c2.append('2')
c2.append(2)

# print(b2)
# print(c2)

def mapping(dict1: Mapping[int, str]) -> list[int]:
    # dict1['3'] = 1
    return list(dict1.keys())

# mapping({1:'1', 2:'2'})

def mapping2(dict1: MutableMapping[int, str]) -> set[str]:
    # dict1['3'] = 1
    return set(dict1.values())

# mapping2({1:'1', 2:'2'})

class MyClass:
    attr: int
    n: int = 100

    def __init__(self, n:int = 0) -> None:
        self.n = n

    def add_n(self) -> int:
        return self.n + self.n

my_class: MyClass = MyClass()

class Car:
    wheels: ClassVar[int] = 4
    model: ClassVar[str] = 'BMW'

class Box:
    def __init__(self) -> None:
        self.items: list[str] = []

def optional1(n: str) -> Optional[int]:
    return int(n) if n.isdigit() else None

# print(optional1('123text'))
# print(optional1('123'))

def print_text(text: str) -> None:
    print(text)

# print_text('Hi, world')

t1: Union[int, str] = 1
t1 = 'text'
# t1 = 1.1