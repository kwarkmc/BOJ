import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

def dfs(c):
    visited[c] = True
    ans_dfs.append(c)
    for n in graph[c]:
        if not visited[n]:
            dfs(n)

def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = True
    ans_bfs.append(s)
    while queue:
        c = queue.popleft()
        for n in graph[c]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True
                ans_bfs.append(n)

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
ans_dfs = list()
ans_bfs = list()

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
dfs(R)
print(*ans_dfs)

visited = [False] * (N + 1)
bfs(R)
print(*ans_bfs)