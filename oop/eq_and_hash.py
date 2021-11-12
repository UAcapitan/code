class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(10,20)
p2 = Point(10,20)
print(p1 == p2)
print(p1.__hash__())
print(p2.__hash__())