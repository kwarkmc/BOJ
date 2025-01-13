import sys

# sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
idx = 1
input_list = list()
stack = []
result_list = []
find = True


for _ in range(n):
    num = int(sys.stdin.readline())
    while idx <= num:
        stack.append(idx)
        result_list.append('+')
        idx += 1
    if stack[-1] == num:
        stack.pop()
        result_list.append('-')
    else:
        find = False

if not find:
    print("NO")
else:
    for i in result_list:
        print(i)
