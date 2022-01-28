def gen():
    try:
        while num < 25:
            num = 5
            print('Number:',num)
            x = yield num
    except StopIteration:
        print('End of work')
    else:
        print('X:', x)
        num += x

g = gen()