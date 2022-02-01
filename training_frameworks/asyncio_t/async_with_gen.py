def counter():
    counter = 0
    while True:
        print(counter)
        counter += 1
        yield

def main():
    g = counter()
    while True:
        next(g)
        yield

if __name__ == '__main__':
    main()