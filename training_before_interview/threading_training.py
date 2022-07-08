import threading
import time
import random

def task():
    n = random.randint(1,11)
    while True:
        time.sleep(n)
        print(f"Success, {str(n)} seconds")

task1 = threading.Thread(target=task)
task2 = threading.Thread(target=task)

task1.start()
task2.start()