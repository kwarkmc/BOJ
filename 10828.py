import sys

# sys.stdin = open("input.txt", "r")

stack = list()
N = int(sys.stdin.readline())

for _ in range(N):
    list_input = list(map(str, sys.stdin.readline().split()))
    command = list_input[0]
    number = 0
    if len(list_input) > 1:
        number = list_input[1]

    if command == "push":
        stack.append(number)
    elif command == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif command == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

