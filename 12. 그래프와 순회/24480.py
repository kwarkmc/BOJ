import sys
# sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)

def dfs(v):
    global cnt
    visited[v] = cnt
    for n in graph[v]:
        if not visited[n]:
            cnt += 1
            dfs(n)


N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
ans_dfs = list()
cnt = 1

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort(reverse=True)

dfs(R)

for i in range(1, N + 1):
    print(visited[i])
