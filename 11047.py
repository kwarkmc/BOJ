import sys

# sys.stdin = open("input.txt", "r")

N, K = map(int, sys.stdin.readline().split())
result = 0

coin_list = list()

for i in range(N):
    coin_list.append(int(sys.stdin.readline()))

for i in range(N - 1, -1, -1):
    temp = K // coin_list[i]
    if temp > 0:
        result += temp
        K = K % coin_list[i]

print(result)