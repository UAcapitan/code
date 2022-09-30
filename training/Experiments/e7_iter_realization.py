
from typing import Any


class MyIter:
    def __init__(self, list_: list):
        self.n: int = 0
        self.obj: list = list_

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.obj) > self.n:
            elem: Any = self.obj[self.n]
            self.n += 1
            return elem
        raise StopIteration("Iteration was stopped")


if __name__ == "__main__":
    obj_iter: MyIter = MyIter([1,2,3,4,5,6,7])
    for i in range(7):
        print(next(obj_iter))
    print(next(obj_iter))
