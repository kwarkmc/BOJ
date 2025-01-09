# import sys
#
# sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

list_input = list()
result = list()

for _ in range(N):
    list_input.append(input())

for i in range(N - 7):  # 잘라서 8 * 8 체스판을 만들 것임. -> outofindex 방지하기 위해 N - 7 만큼 순회
    for j in range(M - 7):
        starts_W = 0
        starts_B = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:    # (a + b) % 2 == 0 를 계산하면 짝/홀에 따라 격자무늬를 판별할 수 있음
                    if list_input[a][b] != 'B':
                        starts_B += 1
                    if list_input[a][b] != 'W':
                        starts_W += 1
                else:
                    if list_input[a][b] != 'W':
                        starts_B += 1
                    if list_input[a][b] != 'B':
                        starts_W += 1
        result.append(starts_B)
        result.append(starts_W)

print(min(result))