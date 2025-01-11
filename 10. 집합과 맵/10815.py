import sys

M = int(input())
card_set = set(map(int, sys.stdin.readline().split()))

N = int(input())
find_set = list(map(int, sys.stdin.readline().split()))

result_list = list()

for item in find_set:
    if item in card_set:
        result_list.append(1)
    else:
        result_list.append(0)

print(*result_list)
