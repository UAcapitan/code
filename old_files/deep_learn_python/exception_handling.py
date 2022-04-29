import os
from typing import final

def open_file():
    n = int(input('Choose your file: '))
    try:
        programs = os.listdir()
        print(programs[n])
    except:
        print('Sorry, but this file not found')
    finally:
        print('See you soon')

open_file()

def check_number():
    n = int(input('Write you number: '))
    try:
        a = 5 / n
        l = [i for i in range(n)]
        print(l[10])
    except ZeroDivisionError:
        print('You input 0')
    except:
        print('You have error')
    else:
        print(n)
    finally:
        print('See you soon')

check_number()
