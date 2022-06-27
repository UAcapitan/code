def calculator(e):
    if len(e) != 3:
        raise ValueError('Incorrect data')
    try:
        a, sym, b = int(e[0]), e[1], int(e[2])
    except ValueError:
        raise ValueError('Incorrect type of data')
    if sym == '+':
        return a + b
    if sym == '-':
        return a - b
    if sym == '*':
        return a * b
    if sym == '/':
        return a / b
