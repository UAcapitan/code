def inc(x):
    return int(x + 1)

def error():
    raise Exception()

def cap(text):
    return text.capitalize()

def some_errors(n):
    try:
        n = n + 'text'
        n = 0 / n
        n += 1
    except:
        raise Exception()
    return 0

def return_num(n):
    if n <= 10:
        return 0
    elif n <= 20:
        raise Exception()
    return n