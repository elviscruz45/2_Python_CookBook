from collections import deque 

import heapq

q=deque()

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

print(q)
print(dir(q))
print(q.popleft())
print(q.popleft())

print(q)
