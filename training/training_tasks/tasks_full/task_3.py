numbers_list = [1,2,3]

numbers_list.clear()

print(numbers_list)

print()

for i in range(1,4):
    numbers_list.append(i)

print(numbers_list)

print()

copy_numbers_list = numbers_list.copy()

print(copy_numbers_list)

print(numbers_list)

copy_numbers_list.clear()

print(copy_numbers_list)

print(numbers_list)

del copy_numbers_list

print()

print(numbers_list.count(2))

print()

numbers_list.extend([4])

print(numbers_list)

del numbers_list[-1]

print(numbers_list)

print()

print(numbers_list.index(2))

print()

numbers_list.insert(2, 4)

print(numbers_list)

del numbers_list[2]

print(numbers_list)

print()

numbers_list.pop()

print(numbers_list)

numbers_list.pop(0)

print(numbers_list)

numbers_list.insert(0,1)

print(numbers_list)

print()

numbers_list.remove(2)

print(numbers_list)

print()

numbers_list.extend([2,3])

numbers_list.reverse()

print(numbers_list)

print()

numbers_list.sort()

print(numbers_list)

numbers_list.sort(reverse=True)

print(numbers_list)

numbers_list.sort(key=abs)

print(numbers_list)

print()