test_num_list = [1,2,3]

new_num_list = [i for i in test_num_list if i % 2 == 0]

print(test_num_list)
print(new_num_list)

new_second_num_list = [i if i > 1 else i + 10 for i in test_num_list]

print(new_second_num_list)

print()

a = lambda i,j: i+j

print(a(1,2))

sort_list = [(10,2),(3,4),(10,25)]

sort_list.sort()

print(sort_list)

sort_list.sort(key=lambda i: i[1])

print(sort_list)

print()

b = [(lambda i: i+i), (lambda i: 0)]

print(b[0](1))
print(b[1](1))

print()

def return_nums():
    my_list = range(5)
    for i in my_list:
        yield i+i

generator = return_nums()

for i in generator:
    print(i)

print()