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
print(list_)
dict_ = {k:b for b, k in {'1':'a', '2':'b', '3':'c'}.items()}
print(dict_)
set_ = {i for i in [1,2,3,4,5,5,5]}
print(set_)
generator_ = (i*2 for i in range(5))
print(generator_)