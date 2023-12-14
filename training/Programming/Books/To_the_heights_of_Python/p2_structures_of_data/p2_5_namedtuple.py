
from collections import namedtuple


City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 129.691667))

print(tokyo)
print(City._fields)
print(tokyo._fields)
