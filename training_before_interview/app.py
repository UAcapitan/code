def gen():
    n = 1
    while True:
        yield n
        n += 1

g = gen()
# print(next(g))
# print(next(g))
# print(next(g))

i = iter([1,2,3])
# for j in i:
#     print(j)

def coroutine():
    n = True
    while True:
        n = yield
        if not n:
            print('Worked')

# cor = coroutine()
# next(cor)
# cor.send(True)
# cor.send(True)
# cor.send(False)

list_ = [i for i in [1,2,3]]
# print(list_)
dict_ = {k:b for b, k in {'1':'a', '2':'b', '3':'c'}.items()}
# print(dict_)
set_ = {i for i in [1,2,3,4,5,5,5]}
# print(set_)
generator_ = (i*2 for i in range(5))
# print(generator_)

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

import os

# os.system('echo Hello world;')
# os.system('echo Test;')

def test(f):
    def wrapTest():
        print('This is work')
        f()
        print("This is end")
    return wrapTest

@test
def new_test():
    print('I am working')

new_test()