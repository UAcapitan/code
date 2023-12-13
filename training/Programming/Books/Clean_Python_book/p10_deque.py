
from collections import deque


q = deque()
q.append("eat")
q.append("sleep")
q.append("work")

print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q.popleft())
