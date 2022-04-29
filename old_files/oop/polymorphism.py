class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rectangle {self.a} * {self.b} = '
    
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Square {self.a} * {self.a} = '

    def get_area(self):
        return self.a**2

class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Circle 3.14 * {self.r} ** 2 = '

    def get_area(self):
        return 3.14 * self.r**2

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
# print(rect1.get_rect_area(), rect2.get_rect_area())

sq1 = Square(5)
sq2 = Square(7)
# print(sq1.get_sq_area(), sq2.get_sq_area())

cir1 = Circle(5)
cir2 = Circle(7)
# print(cir1.get_circle_area(), cir2.get_circle_area())

figures = [rect1, rect2, sq1, sq2, cir1, cir2]
for figure in figures:
    print(figure, figure.get_area())