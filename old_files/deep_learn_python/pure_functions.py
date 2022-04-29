def inputDate(date):
    return 'Today is ' + date

print(inputDate('10/17/2021'))

def test():
    print('It is test')
    return

t = test()
t

def addInDict(x,y,z):
    return {'x':x, 'y':y, 'z':z}

print(addInDict(10,20,50))

def createTuple():
    return 1,2,3,4,5

print(createTuple())

def defaultValues(a,b=19,c=20):
    return a + b + c

print(defaultValues(10,20,10))
print(defaultValues(10))
print(defaultValues(10,20))

def f(*args):
    for i in args:
        print(i)
    return

f([10,20,40])
f(10,58,39,9,4)

def text(t):
    print(f'{t}')
    return

text('Hello')

def textList(t,t2,t3):
    print(f'{t}')
    print(f'{t2}')
    print(f'{t3}')
    return

t_list = ('Hello','It`s','me')
textList(*t_list)

def f(**kwargs):
    for v,k in kwargs.items():
        print(f'{v} -> {k}')
    return

f(a='1', b='2', c='3')

def textDict(t,b,n):
    print(F'{t}')
    print(F'{b}')
    print(F'{n}')
    return

t_dict = {'t': 'Hello', 'b': 'It`s', 'n': 'me'}
textDict(**t_dict)

def oper(x, y, *ignore, op='+'):
    if op == '+':
            return x + y
    elif op == '-':
            return x - y
    elif op == '/':
            return x / y
    else:
            return None

print(oper(3, 4, op='+'))
print(oper(3, 4, op='/'))

def f(a: int, b: int) -> float:
    pass

print(f.__annotations__)

def f() -> 0:
    f.__annotations__['return'] += 1
    print(f.__annotations__['return'])

f()
f()
f()