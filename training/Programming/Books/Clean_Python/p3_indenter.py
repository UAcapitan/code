
class Indenter:
    def __init__(self):
        self.__space = -4

    def __enter__(self):
        self.__space += 4
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__space -= 4

    def print(self, text):
        space = " "*self.__space
        print(f"{space}{text}")


if __name__ == "__main__":
    with Indenter() as indent:
        indent.print("Hi")
        with indent:
            indent.print("Programming")
            with indent:
                indent.print("Cool")
        indent.print("New")
