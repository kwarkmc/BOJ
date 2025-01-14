import sys

N = int(input())

stack = list()

for i in range(N):
    input_data = sys.stdin.readline().split()
    command = int(input_data[0])
    number = int(input_data[1]) if len(input_data) > 1 else None
    if command == 1:
        stack.append(number)
    elif command == 2:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif command == 3:
        print(len(stack))
    elif command == 4:
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif command == 5:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)