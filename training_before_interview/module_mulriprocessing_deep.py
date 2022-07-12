from audioop import mul
import multiprocessing
import time
import random

def calculate(a,b):
    n = random.randint(1,11)
    # while True:
    time.sleep(n)
    print(f"Time sleep: {str(n)}")
    print(f"{str(a)} + {str(b)} = {str(a+b)}")
    print("-"*7)

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = [
        multiprocessing.Process(target=calculate, args=(2,1)),
        multiprocessing.Process(target=calculate, args=(3,4)),
        multiprocessing.Process(target=calculate, args=(3,19)),
    ]

    for i in p:
        i.start()
        i.join()

    print(q.get())