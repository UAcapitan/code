def num_sum(l):
    assert len(l) > 5 
    return sum(l)

print(num_sum([1,2,3,4,5,6,7,8,9,10]))
# print(num_sum([1,2,3]))

def print_num(n):
    assert type(n) == int, 'Not integer'
    return str(n)

print(print_num(10))
# print(print_num('10'))