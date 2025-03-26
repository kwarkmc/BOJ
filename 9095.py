import sys

# sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())   # 테스트 케이스 개수

list_input = [0] * n

for i in range(n):
    list_input[i] = int(sys.stdin.readline())

dp = [0] * (max(list_input) + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max(list_input) + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for i in list_input:
    print(dp[i])

'''
DP 문제에 접근하는 방법
1. 작은 입력부터 손으로 직접 계산하며 예시로부터 규칙 찾기
2. 상태를 정의함으로서 dp[i]가 의미하는 것을 명확히 하기
3. 마지막 선택으로 나누기 - dp[i]가 어떤 상태들로부터 만들어졌는지 찾기
4. 점화식 유도 - 재사용되는 하위 문제들을 합치기
5. 패턴 학습 - 계단 오르기 / 동전으로 금액 만들기 / 숫자 합 조합 / 문자열 편집 거리
'''