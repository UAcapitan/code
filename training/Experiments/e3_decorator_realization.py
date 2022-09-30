
from datetime import datetime


def timer(func):
    def wrap(*args):
        t = datetime.now()
        result = func(*args)
        print("Time:", end=" ")
        print(datetime.now() - t)
        return result
    return wrap

@timer
def test(x, y, z):
    return f"Result: {str(x*y*z)}"


if __name__ == "__main__":
    print(test(10,10,70))
