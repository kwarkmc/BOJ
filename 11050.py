# 이항계수 (N K) -> nCk = n! / (n - k)! * k!

''' math 패키지의 factorial 매서드를 활용한 풀이
import math

N, K = map(int, input().split())

result = math.factorial(N) / (math.factorial(N - K) * math.factorial(K))

print(int(result))
'''

# 이항계수의 성질
# (N K) = (N N - k) -> n개 중 k개를 선택하는 조합의 수는 결국 n개 중 선택받지 못한 아이템의 조합의 수와 같다.
# (N K) = (N - 1 K) + (N - 1 K - 1)

n, k = map(int, input().split())

dp = [[1] * (n + 1) for _ in range(n + 1)]

# DP (Dynamic Programming) -> 같은 작업을 하위부터 계속 수행해야 할 때, DP 테이블에 수행한 값들을 넣어놓고 사용하여 시간을 줄일 수 있다.

for i in range(2, n + 1):
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        # 점화식 C(n, k) = C(n - 1, k - 1) + C(n - 1, k)

print(dp[n][k] % 10007)