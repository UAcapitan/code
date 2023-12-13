
import heapq


q = []

heapq.heappush(q, (2, "sleep"))
heapq.heappush(q, (1, "eat"))
heapq.heappush(q, (3, "work"))

while q:
    print(heapq.heappop(q))
