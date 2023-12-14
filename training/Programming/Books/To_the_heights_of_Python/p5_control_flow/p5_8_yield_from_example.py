
def example():
    yield from "ABC"

if __name__ == "__main__":
    e = example()
    for i in e:
        print(i) 