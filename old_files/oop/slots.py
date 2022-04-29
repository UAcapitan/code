class Rectangle:
    __slots__ = ('__width', 'height')

    def __init__(self, a, b):
        self.width = a
        self.height = b

    # @property
    # def perimetr(self):
    #     return (self.height+self.width)*2

    # @property
    # def area(self):
    #     return self.height * self.width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

class Square(Rectangle):
    __slots__ = ('color')
    def __init__(self, a, b, color):
        super().__init__(a,b)
        self.color = color

b = Rectangle(10,20)
# print(b.area)
# print(b.perimetr)
# print(b.__dict__)
# print(b.width)
squ = Square(10, 10, 'green')
# print(squ.__dict__)
print(squ.width, squ.height, squ.color)