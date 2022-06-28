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

cor = coroutine()
next(cor)
cor.send(True)
cor.send(True)
cor.send(False)
