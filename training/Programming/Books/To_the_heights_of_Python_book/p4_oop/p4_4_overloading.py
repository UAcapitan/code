
import numbers
import itertools


class ListNew:
    def __init__(self, iterable):
        self._list = iterable

    def __str__(self) -> str:
        return f"List([{', '.join([str(i) for i in self._list])}])"

    def __add__(self, object):
        try:
            sum_ = [sum(i) for i in itertools.zip_longest(self._list, object._list, fillvalue=0)]
            return ListNew(sum_)
        except:
            return NotImplemented

    def __radd__(self, object):
        return self + object

    def __mul__(self, object):
        if isinstance(object, numbers.Integral):
            return ListNew([i * object for i in self._list])
        elif isinstance(object, ListNew):
            sum_ = [i[0] * i[1] for i in itertools.zip_longest(self._list, object._list, fillvalue=1)]
            return ListNew(sum_)
        else:
            return NotImplemented

    def __call__(self):
        return self._list


if __name__ == "__main__":
    print(ListNew([1,2,3]))
    print(ListNew([1,2,3])())

    print(ListNew([1,2,3]) + ListNew([1,2,3,4]))
    # print(ListNew([1,2,3]) + [1,2,3])

    print(ListNew([1,2,3]) * 3)
    print(ListNew([1,2,3]) * ListNew([1,2,3]))
    # print(ListNew([1,2,3]) * [1,2,3])
