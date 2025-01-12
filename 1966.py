import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

L = int(sys.stdin.readline())   # 테스트케이스의 수

for _ in range(L):
    N, M = map(int, sys.stdin.readline().split())   # N : 문서의 개수 / M : 원하는 문서의 Index
    queue_doc = deque(map(int, sys.stdin.readline().split()))     # 중요도가 같은 문서가 여러개 있을 수 있다.
    result_count = 0

    while len(queue_doc) > 0:
        if queue_doc[0] == max(queue_doc):
            queue_doc.popleft()
            M -= 1
            result_count += 1
            if M < 0:
                break
        else:
            queue_doc.append(queue_doc.popleft())
            M -= 1
            if M < 0:
                M = len(queue_doc) - 1

    print(result_count)


