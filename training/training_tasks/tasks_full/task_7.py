def decorate(f):
    def wrapper(value):
        print('Work')
        f(value)
    return wrapper

@decorate
def test(n):
    print(n)

test(5)

print()

def numbers(*a):
    a = [str(i) for i in a]
    print(' '.join(a))

numbers(1,2,3)

print()

def main(n):
    print(n)

if __name__ == '__main__':
    main(5)

print()