import sys

# sys.stdin = open("input.txt", 'r')

N, M = map(int, sys.stdin.readline().rstrip().split())

array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

K = int(sys.stdin.readline().rstrip())

for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    result = 0
    for a in range(i - 1, x):
        for b in range(j - 1, y):
            result += array[a][b]
    print(result)