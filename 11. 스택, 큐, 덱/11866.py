from collections import deque

N, K = map(int, input().split())

queue = deque(range(1, N + 1))
result = list()

while len(queue) > 0:
    for i in range(K - 1):
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))

print("<" + ', '.join(result) + ">")
