nums = [5,4,8,1,9,3,6,7,2]

def selection_sort(n):
    new = []
    for i in range(len(n)):
        new.append(n.pop(n.index(min(n))))

    return new

print(selection_sort(nums))