import sys
from collections import deque

# sys.stdin = open("input.txt", 'r')

def bfs(a, b):
    queue = deque()
    queue.append(a)
    visited[a] = 0
    while queue:
        curr = queue.popleft()
        if curr == b:
            return visited[curr]

        for i in nodes[curr]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[curr] + 1
    return -1

n = int(sys.stdin.readline())   # 전체 사람의 수 n
a, b = map(int, sys.stdin.readline().rstrip().split())  # 촌수를 계산해야 하는 두 사람의 번호
m = int(sys.stdin.readline())   # 부모자식 관계의 개수

nodes = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    nodes[u].append(v)
    nodes[v].append(u)

print(bfs(a, b))