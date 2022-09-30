
class A:
    n: str = str(1)

    @classmethod
    def class_foo(cls, x) -> str:
        return f"Obj: {cls.n}\nx: {str(x)}"

    @staticmethod
    def static_foo(x) -> str:
        return f"x: {str(x)}"


if __name__ == "__main__":
    print(A.class_foo(1))

    print()

    print(A.static_foo(1))
