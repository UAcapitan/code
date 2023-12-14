
import contextlib


class ManagerFile:
    def __init__(self, name):
        self.__name = name

    def __enter__(self):
        self.__file = open(f"{self.__name}.txt", "w")
        return self.__file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file.close()

@contextlib.contextmanager
def manager_file(name):
    try:
        file = open(f"{name}.txt", "w")
        yield file
    finally:
        file.close()


if __name__ == "__main__":
    with ManagerFile("test1") as file:
        file.write("Test")

    with manager_file("test2") as file:
        file.write("Test")
