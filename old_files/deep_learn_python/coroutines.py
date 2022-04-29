def coroutine(func):
    def inner():
        g = func()
        g.send(None)
        return g
    return inner

@coroutine
def gen():
        num = 5

        while num < 25:
            try:
                x = yield 'Number ' + str(num)
            except StopIteration:
                break
            else:
                num += x
        
        return num

g = gen()
try:  
    print(g.send(5))
    print(g.send(5))
    print(g.send(5))
    print(g.send(5))
    print(g.send(5))  
    # print(g.throw(StopIteration))
except StopIteration as e:
    print('Result:', e.value)