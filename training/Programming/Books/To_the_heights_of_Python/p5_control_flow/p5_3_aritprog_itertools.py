
import itertools


def airprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    print(ap_gen)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
        print(ap_gen)
    return ap_gen


if __name__ == "__main__":
    gen = airprog_gen(1,2)
    for _ in range(7):
        print(next(gen))