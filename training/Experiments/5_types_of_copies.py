
from copy import deepcopy

list_original: list[int] = [1,2,3,4,5,6,7,8,9]

if __name__ == "__main__":
    list_shallow_copy: list[int] = list_original.copy()
    list_deep_copy: list[int] = deepcopy(list_original)
    
    print(list_original)
    print(list_shallow_copy)
    print(list_deep_copy)
