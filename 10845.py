import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

queue = deque()

for _ in range(N):
    input_list = list(map(str, sys.stdin.readline().split()))
    command = input_list[0]
    number = 0
    if len(input_list) > 1:
        number = input_list[1]

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
        if len(queue) > 0:
            print(0)
        else:
            print(1)
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