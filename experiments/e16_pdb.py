
import pdb


pdb.set_trace()

def func():
    n = 0
    while n < 22:
        n += 1
        pdb.set_trace()
        print(f"Some text, n: {str(n)}")


if __name__ == "__main__":
    func()
