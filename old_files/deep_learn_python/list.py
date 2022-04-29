my_list = [1,2,3,4,5]

my_list.append(10)
print(my_list)

my_list.clear()
print(my_list)

my_list = [1,2,3,4,5]
print(my_list)

ml = my_list.copy()
print(ml)

print(my_list.count(5))

my_list.extend(iter([3,4,5]))
print(my_list)

print(my_list.index(5))

my_list.insert(3, 10)
print(my_list)

my_list.pop(0)
print(my_list)

my_list.remove(5)
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)