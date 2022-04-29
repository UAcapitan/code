from functools import reduce

l = [1, 2, 3, 5, 7]

def reducer_func(el_prev, el):
    return el_prev + el

print(reduce(reducer_func, l))

print(reduce(lambda a,b: a*b, [1,2,3,4,5]))