import itertools

list_ = [
    itertools.accumulate([1,2,3,4,5]),
    itertools.combinations('ABCDF', 3),
    itertools.compress('ABCDF', '01'),
    itertools.dropwhile(lambda x: x < 5, [1,2,3,4,5,6,7,8,9]),
    itertools.product('ABC', 'xy'),
    itertools.takewhile(lambda x: x >= 5, [7,6,5,4,3,2,1]),
    itertools.zip_longest('ABCD', 'xy', fillvalue='-')
]

# for i in list_:
#     print(list(i))