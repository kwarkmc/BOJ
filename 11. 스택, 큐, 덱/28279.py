import sys
from collections import deque
N = int(sys.stdin.readline())

dequeue = deque()

for i in range(N):
    input_data = list(map(int, sys.stdin.readline().split()))
    command = input_data[0]
    number = input_data[1] if len(input_data) > 1 else None

    if command == 1:
        dequeue.appendleft(number)
    elif command == 2:
        dequeue.append(number)
    elif command == 3:
        if len(dequeue) > 0:
            print(dequeue.popleft())
        else:
            print(-1)
    elif command == 4:
        if len(dequeue) > 0:
            print(dequeue.pop())
        else:
            print(-1)
    elif command == 5:
        print(len(dequeue))
    elif command == 6:
        if len(dequeue) == 0:
            print(1)
        else:
            print(0)
    elif command == 7:
        if len(dequeue) > 0:
            print(dequeue[0])
        else:
            print(-1)
    elif command == 8:
        if len(dequeue) > 0:
            print(dequeue[-1])
        else:
            print(-1)

