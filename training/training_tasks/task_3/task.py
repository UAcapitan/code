list_1 = [2,4,5]
list_2 = [6,7,4,2,8]
list_result = []

for i in list_1:
    check = True
    for j in list_2:
        if i == j:
            check = False

    if check:
        list_result.append(i)

print(list_result)