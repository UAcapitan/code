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

# hash ----------------------------------------------------

text = hash('Hello, world')
# print(text)

# hex -----------------------------------------------------

h_text = hex(255)
# print(h_text)

# isistance -----------------------------------------------

x = isinstance(5, int)
y = isinstance(5, str)
# print(x)
# print(y)

# issubclass ----------------------------------------------

class Polygon:
  def __init__(polygonType):
    print('Polygon is a ', polygonType)

class Triangle(Polygon):
  def __init__(self):

    Polygon.__init__('triangle')
    
# print(issubclass(Triangle, Polygon))
# print(issubclass(Triangle, list))
# print(issubclass(Triangle, (list, Polygon)))
# print(issubclass(Polygon, (list, Polygon)))
# print(issubclass(Polygon, list))

# iter ----------------------------------------------------

iter_t = iter(['a','b','c'])
# print(iter_t)

# license -------------------------------------------------

license
# print(license)
# license()

# locals --------------------------------------------------

l = locals()
# print(l)

# map -----------------------------------------------------

def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
# print(list(result))
nums = list(result)
# print(nums)
res = map(lambda x: x+x, nums)
# print(list(res))

# max -----------------------------------------------------

l = [1,2,19,28,41,57,94,184,838,729,2948,392,38,4843,94839]
m = max(l)
# print(m)

# memoryview ----------------------------------------------

random_byte_array = bytearray('ABC', 'utf-8')
# print('Before updation:', random_byte_array)
mv = memoryview(random_byte_array)
# print(list(mv))
mv[1] = 90
# print('After updation:', random_byte_array)

# min -----------------------------------------------------

l = [4,6,9,49,945,35,593,2939,1,3,595,30,49549,398,31]
m = min(l)
# print(m)

# next ----------------------------------------------------

i = iter([1,2,3])
i_1 = next(i)
i_2 = next(i)
i_3 = next(i)
# print('{}, {}, {}'.format(i_1,i_2,i_3))

# oct -----------------------------------------------------

n_o = oct(10)
# print(n_o)

# open ----------------------------------------------------

# f = open('text.txt', 'w')
# print('Test', file=f)
# f.write('Text \n')
# text_list = ['Text_1 \n','Text_2 \n','Text_3 \n']
# f.writelines(text_list)

# all -----------------------------------------------------

l = [True, True, True]
l2 = [True, False, True]
l3 = [1,2,3,4,5]
l4 = ['1', 'a', 'cb']
l5 = [1, 1, 1, [1,1,1]]
l6 = [1,1,1,1,1]
l7 = [1,1,0,1,1]

# print(all(l))
# print(all(l2))
# print(all(l3))
# print(all(l4))
# print(all(l5))
# print(all(l6))
# print(all(l7))

# any -----------------------------------------------------

l1 = [True, True]
l2 = [True, False]
l3 = [False, False]

# print(any(l))
# print(any(l2))
# print(any(l3))

