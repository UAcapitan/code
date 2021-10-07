# Assert --------------------------------------------------

def sum_n(l):
    assert len(l) != 0, 'List is empty'
    return len(l)

# print(sum_n([0,20,30]))
# print(sum_n([]))

# ---------------------------------------------------------

# Lambda --------------------------------------------------

x = lambda x, y, z : x*y*z
# print(x(10,20,30))

# ---------------------------------------------------------

x = 'Mike'

def test_1():
    x = 'Max'
    def test_2():
        nonlocal x
        x = 'Kim'
    test_2()
    return x

# print(test_1())

# ---------------------------------------------------------

# Raise ---------------------------------------------------

def error_1():
    raise Exception('Error 1')

# error_1()

def error_2():
    raise Exception

# error_2()

def error_3():
    raise BaseException('Error 3')

# error_3()

# ---------------------------------------------------------

# With ----------------------------------------------------

def print_in_file():
    with open('newfile.txt', 'w', encoding='utf-8') as g:
        print('Test', file=g)

# ---------------------------------------------------------

# Yield ---------------------------------------------------

def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i

# mygenerator = create_generator()
# print(mygenerator)

# for i in mygenerator:
#     print(i)

# ---------------------------------------------------------