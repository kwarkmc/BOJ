import sys

# sys.stdin = open("input.txt", 'r')

N = int(sys.stdin.readline())

count = 0
for _ in range(N):
    array_input = list(sys.stdin.readline().rstrip())
    stack = []
    for item in array_input:
        if len(stack) == 0:
            stack.append(item)
        elif stack[-1] == item:
            stack.pop()
        else:
            stack.append(item)
    if len(stack) == 0:
        count += 1

print(count)