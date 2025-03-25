import sys

# sys.stdin = open('input.txt', 'r')

A, B, C, D = map(int, sys.stdin.readline().split())
list_input = list(map(int, sys.stdin.readline().split()))

for i in list_input:
    attacked = 0
    if 0 < i % (A + B) <= A:
        attacked += 1
    if 0 < i % (C + D) <= C:
        attacked += 1
    print(attacked)

# 모듈러 연산 % 는 주기를 나타낼 때 주로 사용된다.
# 1분 -> 공격, 2분 -> 공격, 3분 -> 휴식, 4분 -> 휴식의 순으로 돌아가기 때문에
# 0 < i % (A + B) < A 함으로서 (A + B) 총 주기를 i에 모듈러 연산 한 결과가 A (2분) 초과한다면 개가 휴식중인것.
