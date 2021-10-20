import itertools

# itertools.count ----------------------------------
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        # print(i, end =" ")
        pass

# itertools.cycle ----------------------------------

i = itertools.cycle(list('ABC'))
# for x in range(10):
    # print(next(i), end='\n')

# itertools.repeat ---------------------------------
n = 5
i = itertools.repeat(1,n)
# for x in range(n):
#     print(next(i))

# itertools.accumulate -----------------------------

i = itertools.accumulate([1,2,3,4,5])
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))