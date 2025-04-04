import sys

# sys.stdin = open("input.txt", 'r')

N, M = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))
sum_array = [0] * N
sum_array[0] = array[0]
for i in range(N):
    sum_array[i] = sum_array[i - 1] + array[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(sum_array[j - 1])
    else:
        print(sum_array[j - 1] - sum_array[i - 2])