import os

name_file = input('Name file: ')
files = os.listdir('D://')

try:
    for f in files:
        if name_file in f:
            need_file = f
            break
    file = need_file.replace(name_file, '').replace('.','')
    print(file if file != '' else 'Not have type')
except:
    print('Error')