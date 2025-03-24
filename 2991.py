import sys

# sys.stdin = open('input.txt', 'r')

A, B, C, D = map(int, sys.stdin.readline().split())
list_input = list(map(int, sys.stdin.readline().split()))

for i in list_input:
    attacked = 0
    if 0 < i % (A + B) <= A:
        attacked += 1
    if 0 < i % (C + D) <= C:
        attacked += 1
    print(attacked)
