
import bisect


list_ = [3,7,4,8,9,1,5,2,6]
list_.sort()
print(list_)

ind = bisect.bisect(list_, 3)
list_.insert(ind, 3)
print(list_)
