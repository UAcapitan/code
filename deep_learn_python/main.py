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

# ascii ---------------------------------------------------

a = ascii('''Test
is
good!''')
# print(a)

# bin -----------------------------------------------------

b = bin(10)
# print(b)

# bool ----------------------------------------------------

b1 = bool(1)
b2 = bool(0)
b3 = bool('None')
# print(b1)
# print(b2)
# print(b3)

# bytes ---------------------------------------------------

message = 'Python is fun'
byte_message = bytes(message, 'utf-8')
# print(byte_message)
# print(list(byte_message))

# callable ------------------------------------------------

x = 5
# print(callable(x))

def test():
    return 5

# print(callable(test))

# compile -------------------------------------------------

codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')
# print(codeObejct)

# complex -------------------------------------------------

z = complex(10,20)
# print(z)

# enumerate -----------------------------------------------

languages = ['Python', 'Java', 'JavaScript']
enumerate_prime = enumerate(languages)
# print(list(enumerate_prime))

# eval ----------------------------------------------------

n = 9
# print(eval('n * n'))

# exec ----------------------------------------------------

a = 'b = 5\nb += 1\nprint(b)'
# exec(a)

# exit ----------------------------------------------------

# input()
# exit()

# ord -----------------------------------------------------

o = ord('P')

# print(o)

# pow -----------------------------------------------------

p = pow(10,2)

# print(p)

# property ------------------------------------------------

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return 'The name is: ' + self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    name = property(get_name, set_name, del_name)

# p = Person('Adam')
# print(p.name)
# p.name = 'John'
# del p.name

# filter --------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def check_even(number):
    if number % 2 == 0:
          return True  
    return False

even_numbers_iterator = filter(check_even, numbers)
even_numbers = list(even_numbers_iterator)
# print(even_numbers)

# quit ----------------------------------------------------

# input()
# quit()

# repr ----------------------------------------------------

numbers = [1, 2, 3, 4, 5]

printable_numbers = repr(numbers)
# print(printable_numbers)

# reversed ------------------------------------------------

i = reversed('Test')
# print(list(i))

# round ---------------------------------------------------

number = 12.10
number2 = 11.95

rounded_number = round(number)
rounded_number2 = round(number2)
# print(rounded_number)
# print(rounded_number2)

# setattr -------------------------------------------------

class Student:
  marks = 88
  name = 'Sheeran'

person = Student()

setattr(person, 'name', 'Adam')
# print(person.name)

setattr(person, 'marks', 78)
# print(person.marks)

# slice ---------------------------------------------------

text = 'Python Programing'
sliced_text = slice(9)
# print(sliced_text)
# print(text[sliced_text])

# staticmethod --------------------------------------------

class Calculator:

  def add_numbers(num1, num2):
    return num1 + num2

Calculator.add_numbers = staticmethod(Calculator.add_numbers)

sum = Calculator.add_numbers(5, 7)
# print('Sum:', sum)

# super ---------------------------------------------------

class Animal(object):
    def __init__(self, animal_type):
        print('Animal Type:', animal_type)
    
class Mammal(Animal):
    def __init__(self):
        super().__init__('Mammal')
        print('Mammals give birth directly')
    
# dog = Mammal()