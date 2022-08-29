
from functools import reduce

list_ = [1,2,3,4,5,6,7]

list_map = list(map(lambda x: x+1, list_))

list_filter = list(filter(lambda x: x>3, list_))

list_reduce = reduce(lambda x, y: x+y, list_)

if __name__ == "__main__":
    print(list_map)

    print()

    print(list_filter)

    print()
    
    print(list_reduce)
