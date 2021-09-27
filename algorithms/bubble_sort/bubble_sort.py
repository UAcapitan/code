my_list = [3,5,1,2,4,8,7,9,6,0]

def bubble_sort(l):
    for i in range(len(my_list)):
        for i in range(len(my_list)-1, 0, -1):
            if my_list[i-1] > my_list[i]:
                my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
    return l

print(my_list)
print(bubble_sort(my_list))
    