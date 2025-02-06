# 다시 풀어보자!

import sys

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
x, y, direction = map(int, input().split())

visited_map = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

array = []

for i in range(N):
    array.append(list(map(int, input().split())))

visited_map[x][y] = 1   # 시작하는 부분 방문 처리
count = 1
turn_time = 0

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if visited_map[nx][ny] == 0 and array[nx][ny] == 0: # 회전한 후 정면에 가보지 않은 칸이 존재하는 경우
        visited_map[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:   # 회전했지만 가보지 않은 칸이 없거나 바다일 때
        turn_time += 1
    if turn_time == 4:  # 네 면 다 갈 수 없는 경우
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(count)







