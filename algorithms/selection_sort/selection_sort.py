my_list = [1,0,3,6,5,7,9,8,2,4]

def selection_sort(l_old):
    l = []
    for i in range(len(l_old)):
        m = min(l_old)
        n = l_old.index(m)
        l_old.pop(n)
        l.append(m)
    return l

print(selection_sort(my_list))