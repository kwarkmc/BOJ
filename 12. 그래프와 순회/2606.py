import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

def bfs(c):
    global cnt
    queue = deque()
    queue.append(c)
    visited[c] = True
    while queue:
        c = queue.popleft()
        for n in graph[c]:
            if not visited[n]:
                cnt += 1
                queue.append(n)
                visited[n] = True

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(1)

print(cnt)