n = 7

def coutdown(i):
    print(i)
    if i <= 0:
        return
    else:
        coutdown(i-1)

if __name__ == '__main__':
    coutdown(n)