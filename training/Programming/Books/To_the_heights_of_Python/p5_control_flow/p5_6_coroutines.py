
def gen_coroutine():
    n = None
    while True:
        n = yield n

def sum_coroutine():
    sum_ = 0
    while True:
        n = yield sum_
        sum_ += n

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
    gc = gen_coroutine()
    next(gc)
    print(gc.send(10))
    print(gc.send(40))
    print(gc.send(50))
    print()

    sc = sum_coroutine()
    next(sc)
    print(sc.send(10))
    print(sc.send(40))
    print(sc.send(50))
    print()

    ac = average_coroutine()
    next(ac)
    print(ac.send(10))
    print(ac.send(40))
    print(ac.send(50))
