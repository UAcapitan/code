
def chain(*iterables):
    for it in iterables:
        print(it)
        for i in it:
            yield i

def chain_yield(*iterables):
    for i in iterables:
        print(i)
        yield from i


if __name__ == "__main__":
    str_ = "ABC"
    int_ = [1,2,3]

    for i in chain(str_, int_):
        print(i)

    print()

    for i in chain_yield(str_, int_):
        print(i)
