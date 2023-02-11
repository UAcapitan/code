
import copy


list_ = [1,2,3,4,5,6,7]

list_2 = copy.copy(list_)
list_3 = copy.deepcopy(list_)

list_.append(17)

print(list_2, list_3)
