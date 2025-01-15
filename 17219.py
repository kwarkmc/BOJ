import sys

# sys.stdin = open("input.txt", "r")

N, M = map(int, sys.stdin.readline().split())
pw_dict = dict()

for i in range(N):
    site, pw = map(str, sys.stdin.readline().split())
    pw_dict[site] = pw

for i in range(M):
    print(pw_dict[sys.stdin.readline().rstrip()])