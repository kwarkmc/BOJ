import sys

# sys.stdin = open("input.txt", "r")

M = int(sys.stdin.readline())

# 비트마스킹을 통한 풀이

S = 0

for i in range(M):
    A = sys.stdin.readline().strip()
    if A == "all":
        S = (1 << 21) - 1
        # (1 << 21)은 2의 21승을 의미, 21개의 비트로 이루어진 이진수가 된다. 하나를 빼면 20번째 비트까지 모두 1로 설정한다.
    elif A == "empty":
        S = 0
    else:
        command, number = A.split()
        number = int(number)
        if command == "add":
            S |= (1 << number)
            # number 번째 비트는 1로 설정하고 나머지 비트는 유지한다
        elif command == "remove":
            S &= ~(1 << number)
            # number 번째 비트는 0으로 설정하고 나머지는 유지한다
        elif command == "check":
            print(1 if S & (1 << number) != 0 else 0)
            # S & (1 << number) -> number 번째 비트가 1인지 확인한다.
        elif command == "toggle":
            S ^= (1 << number)
            # ^= 연산자는 (1 << number) 번째 비트를 토글시킨다.


'''
# 집합을 사용한 풀이 (통과)
S = set()

for _ in range(M):
    input_list = list(map(str, sys.stdin.readline().split()))
    command = input_list[0]
    number = 0
    if len(input_list) > 1:
        number = input_list[1]

    if command == "add":
        if number not in S:
            S.add(number)
    elif command == "remove":
        S.discard(number)
    elif command == "check":
        if number in S:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if number in S:
            S.discard(number)
        else:
            S.add(number)
    elif command == "all":
        # S = set(range(1, 21))
        S = set(str(i) for i in range(1, 21))
        # print(S)
    elif command == "empty":
        S = set()
        # print(S)
'''