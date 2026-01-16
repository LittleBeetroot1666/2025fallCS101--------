from collections import deque
queue = deque([[0, 0]])
print(queue)
queue.append([0, 1])
print(queue)
queue.append([1, 0])
print(queue)
queue.popleft()
print(queue)
print([0, 0] in queue)
for _ in queue:
    print(_)
print(len(queue))
