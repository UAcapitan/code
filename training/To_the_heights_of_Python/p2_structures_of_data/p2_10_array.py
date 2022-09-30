
from random import random
from array import array


floats = array('d', (random() for _ in range(10*7)))

print(floats[-1])

with open("floats.bin", "wb") as file:
    floats.tofile(file)
    print(file.read())

floats2 = array('d')

with open("floats.bin", "rb") as file:
    floats2.fromfile(file, 10**7)

print(floats2[-1])

print(floats == floats2)
