import sys

sys.stdin = open("input.txt", 'r')

n = int(input())
array_stock = set(map(int, input().split()))
# 집합을 이용해 문제를 해결할 수도 있다.

m = int(input())
array_req = list(map(int, input().split()))

for i in array_req:
    if i in array_stock:
        print("yes", end=' ')
    else:
        print("no", end=' ')
