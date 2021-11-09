import copy

l = [1,2,3,[1,2,3],'abc']

nl_s = copy.copy(l)

nl_d = copy.deepcopy(l)

print(l)
print(nl_s)
print(nl_d)