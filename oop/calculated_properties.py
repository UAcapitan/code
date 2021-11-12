class Square:
    def __init__(self, side):
        self.__side = side
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.__side**2
        return self.__side**2

n1 = Square(10)
print(n1.area)
n1.side = 15
print(n1.area)