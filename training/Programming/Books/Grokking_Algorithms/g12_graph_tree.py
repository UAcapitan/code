from collections import deque

graph = {
    "Wake up": ["Wash up", "Brush teeth"],
    "Wash up": ["To pack", "Take food"],
    "To pack": [],
    "Take food": ["Go to work"],
    "Go to work": [],
    "Brush teeth": ["Eat"],
    "Eat": []
}

q = deque()
list_of_tasks = ["Wake up"]
q += graph[list_of_tasks[0]]

while q:
    task = q.popleft()
    list_of_tasks.append(task)
    q += graph[task]

for i in list_of_tasks:
    print(i)