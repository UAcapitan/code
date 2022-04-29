def create_list(*args):
    return [i for i in args]

x = 5
res = create_list('1', 2, True, x, [1,2,3])
print(res)

list_words = ['Hello', 'world']

def print_text(a,b):
    return a + ' ' + b

t = print_text(*list_words)
print(t)

def create_dict(**kwargs):
    return kwargs

result_cd = create_dict(a=5, b=7, c=3)
print(result_cd)

def print_dict(a, b, c):
    return a + ' ' + b + ' ' + c

my_dict = {'a':'It', 'b':'is', 'c':'easy'}
t_cd = print_dict(**my_dict)
print(t_cd)