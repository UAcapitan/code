# assert --------------------------------------------------

def sum_n(l):
    assert len(l) != 0, 'List is empty'
    return len(l)

# print(sum_n([0,20,30]))
# print(sum_n([]))

# lambda --------------------------------------------------

x = lambda x, y, z : x*y*z
# print(x(10,20,30))

# nonlocal ------------------------------------------------

x = 'Mike'

def test_1():
    x = 'Max'
    def test_2():
        nonlocal x
        x = 'Kim'
    test_2()
    return x

# print(test_1())

# raise ---------------------------------------------------

def error_1():
    raise Exception('Error 1')

# error_1()

def error_2():
    raise Exception

# error_2()

def error_3():
    raise BaseException('Error 3')

# error_3()

# with ----------------------------------------------------

def print_in_file():
    with open('newfile.txt', 'w', encoding='utf-8') as g:
        print('Test', file=g)

# yield ---------------------------------------------------

def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i

# mygenerator = create_generator()
# print(mygenerator)

# for i in mygenerator:
#     print(i)

# abc -----------------------------------------------------

def m(n):
    return abs(n)

# print(m(-5))

# format --------------------------------------------------

def f(name):
    return 'Hello, {}'.format(name)

# print(f('Mike'))

# frozenset -----------------------------------------------

f = frozenset('Mike')

# print(f)

# getattr -------------------------------------------------

class User:
    name = 'Andrey'
    age = 50

user = User()

# print(getattr(user, 'name'))
# print(getattr(user, 'age'))

# globals -------------------------------------------------

# print(globals())

globals()['test'] = 10

# print(globals())

# hasattr -------------------------------------------------

# print(hasattr(user, 'name'))
# print(hasattr(user, 'job'))