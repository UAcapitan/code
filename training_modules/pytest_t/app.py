from typing import Union

def inc(x: Union[int, float]) -> int:
    return int(x + 1)

def error() -> Exception:
    raise Exception()

def cap(text: str) -> str:
    return text.capitalize()

def some_errors(n: int) -> Union[int, Exception]:
    try:
        n += 1
    except:
        raise Exception()
    return 0

def return_num(n: int) -> Union[int, Exception]:
    if n <= 10:
        return 0
    elif n <= 20:
        raise Exception()
    return n

class Calculator:
    def __init__(self, n: int) -> None:
        self.__n: int = n

    def set_n(self, n: int) -> None:
        self.__n = n

    def get_n(self) -> int:
        return self.__n

    def add(self, n: int) -> None:
        self.set_n(self.get_n() + n)