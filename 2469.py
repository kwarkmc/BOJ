import sys

# sys.stdin = open("input.txt", 'r')

k = int(sys.stdin.readline())   # 참가한 사람의 수
n = int(sys.stdin.readline())   # 가로열의 개수

array_answer = list(sys.stdin.readline().rstrip())
array_start = [chr(item) for item in range(65, 65 + k)]
array_input = [[] for _ in range(n)]

for i in range(n):
    array_input[i] = sys.stdin.readline().rstrip()

index_to_find = array_input.index('?' * (k - 1))    # 맞춰야 하는 열이 있는 위치

# 맞춰야 하는 열 위까지 시뮬레이션
simul_above = list(array_start)

for i in range(index_to_find):
    for j in range(k - 1):
        if array_input[i][j] == '-':
            simul_above[j], simul_above[j + 1] = simul_above[j + 1], simul_above[j]

# 아래에서 맞춰야 하는 열 아래까지 시뮬레이션
simul_below = list(array_answer)

for i in range(n - 1, index_to_find, -1):
    for j in range(k - 1):
        if array_input[i][j] == "-":
            simul_below[j], simul_below[j + 1] = simul_below[j + 1], simul_below[j]

array_target = []

i = 0
while i < k - 1:
    if simul_above[i] == simul_below[i]:
        array_target.append('*')
        i += 1
    elif simul_above[i] == simul_below[i + 1] and simul_above[i + 1] == simul_below[i]:
        array_target.append('-')
        array_target.append('*')
        i += 2
    else:
        print('x' * (k - 1))
        break

print(''.join(array_target[:k-1]))