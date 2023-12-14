
class A:
    def print(self):
        print("Class A")

class B(A):
    def str(self):
        print("Class B")

class C(B):
    def print(self):
        print("Class C")
        self.str()
        super().print()
        A.print(self)


if __name__ == "__main__":
    class_ = C()
    print(class_.__class__.__mro__)

    class_.print()
