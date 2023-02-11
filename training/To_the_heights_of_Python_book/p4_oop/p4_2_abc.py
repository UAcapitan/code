
import abc
import random


class Random(abc.ABC):
    
    @abc.abstractmethod
    def load(self, iterable):
        pass

    @abc.abstractmethod
    def pick(self):
        pass

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class Fake(Random):
    def pick(self):
        return 42


class NewRandom(Random):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty NewRandom")
    
    def __call__(self):
        return self.pick()


class SecondRandom(Random):
    def __init__(self, iterable):
        self._items = list(iterable)

    def load(self, iterable):
        self._items.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._items))
        except ValueError:
            raise LookupError("pick from empty SecondRandom")
        return self._items.pop(position)
    
    def loaded(self):
        return bool(self._items)

    def inspect(self):
        return tuple(sorted(self._items))


@Random.register
class ListRandom(list):
    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError("pop from empty ListRandom")

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


if __name__ == "__main__":
    # rand = Random()


    # print(Fake)
    # f = Fake()


    new_rand = NewRandom([1,2,3,4,5,6,7])
    print(new_rand())


    second_rand = SecondRandom([])
    # print(second_rand.pick())
    second_rand.load([1,2,3])
    print(second_rand.pick())
    print(second_rand.loaded())
    print(second_rand.inspect())


    list_rand = ListRandom([])
    # print(list_rand.pick())
    list_rand.load([1,2,3])
    print(list_rand.pick())
    print(list_rand.loaded())
    print(list_rand.inspect())
