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

# itertools.compress -------------------------------
i = itertools.compress('ABCDF', [1,1,0,0,1])

# for x in i:
#     print(x, end=" ")

# itertools.product --------------------------------
i = itertools.product('ABCD', 'AB')

# for x in i:
#     print(x[0] + x[1], end=" ")

# itertools.takewhile ------------------------------
i = itertools.takewhile(lambda x: x < 10, [1,2,3,5,10,15,19,95,290,398])

# for x in i:
#     print(x, end=" ")

# itertools.zip_longest ----------------------------
i = itertools.zip_longest('ABC', 'AB', fillvalue='-')

# for x in i:
#     print(x[0]+x[1], end=" ")