from collections import deque
import sys

N = int(sys.stdin.readline())

queue = deque(enumerate(map(int, sys.stdin.readline().split())))
result_list = list()

while queue:
    idx, rotate = queue.popleft()
    result_list.append(str(idx + 1))

    if rotate > 0:
        queue.rotate(-(rotate - 1))
    elif rotate < 0:
        queue.rotate(-rotate)

print(' '.join(result_list))