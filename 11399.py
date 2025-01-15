import sys

# sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

list_withdraw = list(map(int, sys.stdin.readline().split()))

list_withdraw.sort()
temp = 0
result = 0

for i in range(N):
    result += temp + list_withdraw[i]
    temp += list_withdraw[i]

print(result)