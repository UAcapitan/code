blind_list = []
numbers_list = [1,2,3]

print(any(blind_list))
print(any(numbers_list))

print()

true_list = [True, 1, 'abc']
false_list = [True, False, 0]

print(all(true_list))
print(all(false_list))

print()

def numbers_operations(n):
    return n + 10

nums_list = [10,20,30]

new_nums_list = list(map(numbers_operations, nums_list))

print(new_nums_list)

letters_list = ['abc','b','c']

def filter_function(string):
    return 'b' in string

new_letters_list = list(filter(filter_function, letters_list))

print(new_letters_list)

print()

sort_list = [1,-5,4,7,2]

print(sorted(sort_list))
print(sorted(sort_list, reverse=True))
print(sorted(sort_list, key=abs))