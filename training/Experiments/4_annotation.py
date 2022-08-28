
def test(x: int, y: int, z: int) -> int:
    return x*y*z

def add_text(data: int) -> list:
    return [f"Result: {str(data)}", data]

def result(data: int) -> list[int]:
    return [int(i) for i in str(data)]

if __name__ == "__main__":
    n_list: list[int] = [10,10,70]
    number: int = test(*n_list)
    text_list: list = add_text(number)
    data: list[int] = result(text_list[1])

    print(text_list[0])
    print(data)
