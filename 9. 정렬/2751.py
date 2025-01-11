import sys

numbers = list()

N = int(input())

for i in range(N):
    numbers.append(int(sys.stdin.readline()))

for i in sorted(numbers):
    print(i)
