import sys
from collections import deque

sys.stdin = open("input.txt", 'r')

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    # M : 배추밭의 가로 길이, N : 배추밭의 세로 길이, K : 배추가 심어져있는 개수

    array = [[0] * N for _ in range(M)]
    # [[0] * N] * M 으로 하게 되면 [0] * N에 대한 참조를 M개 만드는 것임.

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        array[x][y] = 1

    count = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(M):
        for j in range(N):
            if array[i][j] == 1:
                count += 1
                queue = deque()
                queue.append((i, j))
                array[i][j] = 0
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        #   nx, ny를 먼저 계산한 후, 범위에서 벗어나서 index 에러가 발생하지 않는지 확인할것.
                        if 0 <= nx < M and 0 <= ny < N:
                            if array[nx][ny] == 1:
                                queue.append((nx, ny))
                                array[nx][ny] = 0
                # bfs로 탐사.
                # 방문한 곳은 그냥 array = 0 처리 하면 될듯.

    print(count)