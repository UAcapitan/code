import multiprocessing
import time
import random

def task():
    n = random.randint(1,11)
    while True:
        time.sleep(n)
        print(f"Success, {str(n)} seconds")

task1 = multiprocessing.Process(target=task)
task2 = multiprocessing.Process(target=task)

# task1.start()
# task2.start()