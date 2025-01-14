import sys
from collections import deque

N = int(input())

queue = deque()

for i in range(N):
    input_data = sys.stdin.readline().split()

    command = input_data[0]
    number = int(input_data[1]) if len(input_data) > 1 else None

    if command == "push":
        queue.append(number)
    elif command == "pop":
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif command == "back":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)