
from queue import PriorityQueue


q = PriorityQueue()

q.put((2, "sleep"))
q.put((1, "eat"))
q.put((3, "work"))

while not q.empty():
    print(q.get())
