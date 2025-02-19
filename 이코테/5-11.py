import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # 현재 위치인 x, y로 부터 네 방향으로의 위치를 확인해야 한다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문할 때만 최단 거리를 기록한다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                # 각 다음 노드에 이전까지 지나온 노드값 + 1 하므로서 graph 2차원 배열에 값이 쌓여 마지막 출구에 최단 거리가 자연스럽게 할당되게 한다.
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))