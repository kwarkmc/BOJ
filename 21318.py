import sys

# sys.stdin = open("input.txt", 'r')

N = int(sys.stdin.readline().rstrip())  # 악보의 개수 N
level = list(map(int, sys.stdin.readline().rstrip().split()))   # 난이도
Q = int(sys.stdin.readline().rstrip())  # 질문의 개수

mistake = [0] * N

for i in range(1, N):
    mistake[i] = mistake[i - 1] + (1 if level[i - 1] > level[i] else 0)

for _ in range(Q):
    count = 0
    x, y = map(int, sys.stdin.readline().rstrip().split())
    print(mistake[y - 1] - mistake[x - 1])