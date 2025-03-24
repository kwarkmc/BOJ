import sys

# sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())   # 파댕이를 돌봐야 하는 시간
N = int(sys.stdin.readline())   # 가지고 있는 사탕의 개수

list_candy = list(map(int, sys.stdin.readline().split()))

for i in list_candy:
    T -= i

if T <= 0:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")