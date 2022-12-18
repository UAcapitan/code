
from math import hypot


# Tests
def test_vector():
    v1 = Vector(2, 5)
    v2 = Vector(2, 2)

    assert v1 == 'Vector(2,5)'
    assert v2 == 'Vector(2,2)'
    assert v1 + v2 == 'Vector(4,7)'
    assert v1 + v2 == Vector(4,7)
    assert abs(v1) == 5.39
    assert bool(v1)
    assert Vector(2,2) * 2 == Vector(4,4)


# Code
class Vector:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
    
    def __add__(self, obj):
        return Vector(self._x + obj._x, self._y + obj._y)

    def __str__(self):
        return f'Vector({self._x},{self._y})'

    def __repr__(self):
        return f'Vector({self._x},{self._y})'

    def __abs__(self):
        return round(hypot(self._x, self._y), 2)

    def __mul__(self, scalar):
        return Vector(self._x * scalar, self._y * scalar)

    def __bool__(self):
        return bool(abs(self._x))

    def __eq__(self, obj):
        try:
            return (self._x == obj._x) and (self._y == obj._y)
        except:
            return str(self) == obj
