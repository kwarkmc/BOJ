import sys

# sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())

print("Gnomes:")
for _ in range(N):
    list_input = list(map(int, sys.stdin.readline().split()))
    if list_input == sorted(list_input) or list_input == sorted(list_input, reverse=True):
        print("Ordered")
    else:
        print("Unordered")
