import sys
# sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)

def dfs(c):
    global cnt
    visited[c] = cnt
    for n in adj[c]:
        if not visited[n]:
            cnt += 1
            dfs(n)


N, M, R = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
ans_dfs = list()
cnt = 1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(N + 1):
    adj[i].sort()

dfs(R)

for i in range(1, N + 1):
    print(visited[i])
