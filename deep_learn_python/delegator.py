def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

def gen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print('........', message)
    return 'Returned from gen'

@coroutine
def delegator(g):
    result = yield from g
    print(result)

sg = gen()
g = delegator(sg)
g.send('Test')
g.send('Test2')
g.send('Test3')
try:
    g.throw(StopIteration)
except StopIteration:
        print('Stop iteration')