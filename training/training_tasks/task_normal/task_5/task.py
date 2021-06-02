num_row = input('n1,n2,n3...: ')

try:
    list_num_1 = num_row.split(',')
    list_num = []
    for i in list_num_1:
        list_num.append(int(i))
    tuple_num = tuple(list_num)
    print(list_num)
    print(tuple_num)
except:
    print('Error')