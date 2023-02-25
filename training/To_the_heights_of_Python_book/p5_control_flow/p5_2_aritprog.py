
def airprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


if __name__ == "__main__":
    gen = airprog_gen(1,2)
    for _ in range(7):
        print(next(gen))
