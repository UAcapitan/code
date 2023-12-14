
from multiprocessing import Queue


q = Queue()
q.put("eat")
q.put("sleep")
q.put("work")

print(q.get())
print(q.get())
print(q.get())
print(q.get()) # waiting
