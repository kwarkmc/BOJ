import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)

def bfs(s):
    global cnt
    queue = deque()
    queue.append(s)
    visited[s] = cnt
    while queue:
        c = queue.popleft()
        for n in graph[c]:
            if not visited[n]:
                cnt += 1
                queue.append(n)
                visited[n] = cnt


N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 1

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

bfs(R)

for i in range(1, N + 1):
    print(visited[i])
