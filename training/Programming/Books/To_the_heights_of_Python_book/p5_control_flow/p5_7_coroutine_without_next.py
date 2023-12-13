
from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def average_coroutine():
    total = 0
    count = 0
    average = 0
    while True:
        n = yield average
        total += n
        count += 1
        average = int(round(total/count, 0))


if __name__ == "__main__":
    ac = average_coroutine()
    print(ac.send(10))
    print(ac.send(40))
    print(ac.send(50))
