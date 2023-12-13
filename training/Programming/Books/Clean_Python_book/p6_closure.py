
def func1(num):
    n = num
    def func2(x):
        nonlocal n
        n += x
        return n
    return func2

if __name__ == "__main__":    
    f = func1(0)
    print(f(4))
    print(f(2))
    print(f(1))
