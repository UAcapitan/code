
from functools import singledispatch


@singledispatch
def main_function(name):
    return f"Hi, {name}!"

@main_function.register(int)
def _(n):
    return f"It's number {str(n)}"

@main_function.register(list)
def _(list_):
    return ", ".join(list_)


if __name__ == "__main__":
    print(main_function("Mike"))
    print(main_function(17))
    print(main_function(["Test", "data", "collection"]))
