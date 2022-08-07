class Test:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def sum_all(self):
        return self.a + self.b + self.c

    def __str__(self):
        return str(self.sum_all())

# test = Test(1,7,2)
# print(test.sum_all())
# print(test)

class Test2(Test):
    def sum_all(self):
        return 0

# test = Test2(1,7,2)
# print(test)

class Test:
    def __init__(self, a):
        self.a = a

    def __getitem__(self, i):
        return self.a[i]

# test = Test({'a':'a', 'b':'b', 'c':'c'})
# print(test['a'])

class Test3(Test2, Test):
    pass

ttt = Test3({'a':'a', 'b':'b', 'c':'c'})