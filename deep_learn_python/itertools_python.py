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
i = itertools.repeat(1,5)

# for x in i:
#     print(x)

# itertools.accumulate -----------------------------
i = itertools.accumulate([1,2,3,4,5])

# for x in i:
#     print(x)

# itertools.chain ----------------------------------
i = itertools.chain([1,2,3], [123,456,789], [9,8,7])

# for x in i:
#     print(x)

# itertools.combinations ---------------------------
i = itertools.combinations('ABCDF', 2)

# for x in i:
#     print('{}{}'.format(x[0], x[1]))

# itertools.combinations_with_replacement ----------
i = itertools.combinations_with_replacement('ABCDF', 2)

# for x in i:
#     print('{}{}'.format(x[0], x[1]))