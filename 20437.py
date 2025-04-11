import sys
from collections import defaultdict

# sys.stdin = open("input.txt", 'r')

T = int(sys.stdin.readline())   # 문자열 게임의 수 T
for _ in range(T):
    W = list(sys.stdin.readline().rstrip())     # 문자열 W
    K = int(sys.stdin.readline())       # 양의 정수 K

    positions = defaultdict(list)
    for i, ch in enumerate(W):
        positions[ch].append(i)

    min_length = 10001
    max_length = -1

    for ch in positions:
        pos_list = positions[ch]
        if len(pos_list) < K:
            continue

        for i in range(len(pos_list) - K + 1):
            start = pos_list[i]
            end = pos_list[i + K - 1]
            length = end - start + 1
            min_length = min(min_length, length)
            max_length = max(max_length, length)

    if max_length == -1:
        print(-1)
    else:
        print(min_length, max_length)

