
class Add:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        self.n += x
        return self.n
    
if __name__ == "__main__":
    a = Add(1)
    print(a(2))
    print(a(2))
    print(a(2))

    str_ = "Text"
    print(callable(a), "-", a)
    print(callable(str_), "-", str_)
