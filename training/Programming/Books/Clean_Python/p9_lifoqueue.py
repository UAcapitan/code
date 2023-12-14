
from queue import LifoQueue


s = LifoQueue()
s.put("eat")
s.put("sleep")
s.put("work")

print(s.get())
print(s.get_nowait())
print(s.get_nowait())
print(s.get_nowait())
