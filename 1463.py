X = int(input())

# DP를 사용해
dp = [0] * 1000001

for i in range(2, X + 1):
    dp[i] = dp[i - 1] + 1   # -1 하는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)  # 2로 나누는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)  # 3으로 나누는 경우

print(dp[X])


