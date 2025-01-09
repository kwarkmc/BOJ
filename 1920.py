# import sys
#
# sys.stdin = open("input.txt", "r")

N = int(input())
# list_A = list(map(int, input().split()))  list로 in 을 사용할 경우, 모든 경우를 순회해야 해서 O(n)이다
set_A = set(map(int, input().split()))      # set으로 in을 사용할 경우 Best O(1) Wort O(n) 으로 더 빠르다.
M = int(input())
list_B = list(map(int, input().split()))

for i in list_B:
    if i in set_A:
        print(1)
    else:
        print(0)