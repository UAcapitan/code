class Num:
    def __init__(self, n):
        self.num = n

    def __len__(self):
        return self.num

    def __abs__(self):
        return 0

n = Num(5)
print(len(n))
print(abs(n))