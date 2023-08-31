
# Creating class
class FirstClass:
    def __init__(self):
        self.n: int = 3
    
    # Encapsulation
    def __add_test(self, new: int) -> int:
        self.n += 1
        self.new: int = new
        return self.n

# Inheritance
class SecondClass(FirstClass):
    def __init__(self) -> None:
        super().__init__()

# Polymorphism
class ThirdClass(SecondClass):
    def __add_test(self, new: int) -> int:
        new += 1
        self.n += new - 2
        return self.n

    def get_result(self, new: int) -> int:
        return self.__add_test(new)

if __name__ == "__main__":
    obj_1 = FirstClass()
    
    obj_2 = SecondClass()

    obj_3 = ThirdClass()
    print(obj_3.get_result(1))
