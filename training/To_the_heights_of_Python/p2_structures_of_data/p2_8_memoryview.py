
from array import array


a = array("I", [1,2,3,4,5,6,7])
m = memoryview(a)
print(list(m))

m_oct = m.cast("B")

print(m_oct.tolist())
