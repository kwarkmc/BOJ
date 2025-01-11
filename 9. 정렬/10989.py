import sys

N = int(input())

lst = [0] * 10001

for i in range(N):
    temp = int(sys.stdin.readline())
    lst[temp] += 1

for i in range(10001):
    if lst[i] is not 0:
        for j in range(lst[i]):
            print(i)