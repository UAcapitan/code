num = int(input('Number: '))

num_list = []

while num > 0:
    num_list.append(num % 2)
    num = num // 2

num_list.reverse()

str_num_list = []

for n in num_list:
    str_num_list.append(str(n))

print(''.join(str_num_list))