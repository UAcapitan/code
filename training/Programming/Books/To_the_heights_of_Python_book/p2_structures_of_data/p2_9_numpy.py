import numpy
from time import perf_counter as pc


# Work with matrix, ndarray and numpy
a = numpy.arange(12)

print(type(a))
print(a)
print(a.shape)

a.shape = 3,4
print(a)
print(a[2])
print(a[2,1])

a.transpose()
print(a)

# Work with files
floats = numpy.loadtxt("floats.txt")
print(floats[-3:])

floats *= .5
print(floats[-3:])

t = pc()
floats /= 3
print(pc() - t)

numpy.save("floats-10M", floats)
floats2 = numpy.load("floats-10M.npy", "r+")
floats2 *= 3
print(floats2[-3:])