import sys
from collections import deque

# sys.stdin = open("input.txt", 'r')

N = int(sys.stdin.readline())   # 주어진 노드의 개수

node = [[] for _ in range(N + 1)]

for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    node[u].append(v)
    node[v].append(u)

parent = [0] * (N + 1)
visited = [False] * (N + 1)

queue = deque()
queue.append(1)
visited[1] = True

while queue:
    curr = queue.popleft()
    for neighbor in node[curr]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = curr
            queue.append(neighbor)

for i in range(2, N + 1):
    print(parent[i])
