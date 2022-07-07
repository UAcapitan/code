a1 = 7
b1 = 7
# print(id(a1), id(b1))
# print(a1 is b1)

a2 = 700
b2 = 700
# print(id(a2), id(b2))
# print(a2 is b2)

class Test:
    def __init__(self):
        self.test = 5
    
    def get_test(self):
        return self.test

class Test2:
    pass

t1 = Test()
t2 = Test()
t3 = Test2()

# print(id(t1))
# print(id(t2))
# print(id(t3))

# print(t1 is t2)
# print(t1 is t3)

t1 = 'Test'
t2 = 'Test'
t3 = 'test'

# print(id(t1))
# print(id(t2))
# print(id(t3))

# print(t1 is t2)
# print(t1 is t3)