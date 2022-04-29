from typing import Type


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if isinstance(item, int):
            if 0<=item<len(self.values):
                return self.values[item]
            else:
                raise IndexError('Index out of range')
        else:
            raise TypeError('Int type needed')

    def __setitem__(self, key, value):
        if isinstance(key, int):
            if 0<=key<len(self.values):
                self.values[key] = value
            elif key>len(self.values):
                diff = key-len(self.values)
                self.values.extend([0]*diff)
                self.values.append(0)
                self.values[key] = value
            else:
                raise IndexError('Index out of range')
        else:
            raise TypeError('Int type needed')

    def __delitem__(self, item):
        if isinstance(item, int):
            if 0<=item<len(self.values):
                del self.values[item]
            else:
                raise IndexError('Index out of range')
        else:
            raise TypeError('Int type needed')

v1 = Vector(1,15,79,98,102)
print(v1)
v2 = Vector(5,2,0,1)
print(v2)
print(v2[1])
# print(v2[-1])
# print(v1['p'])
v1[1] = 5
print(v1)
del v1[2]
print(v1)
v1[16] = 10
print(v1)
v3 = Vector(1)
print(v3)
v3[2] = 10
print(v3)