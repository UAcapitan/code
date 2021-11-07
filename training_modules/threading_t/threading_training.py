import threading
import time

def one(n):
    time.sleep(n)

t1 = threading.Thread(target=one, args=(5,))
t2 = threading.Thread(target=one, args=(3,))

x1 = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

x2 = time.time()

print(x2-x1)