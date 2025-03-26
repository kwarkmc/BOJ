import sys

# sys.stdin = open("input.txt", 'r')

N = int(sys.stdin.readline())   # 계단의 개수

list_stair = list()

for _ in range(N):
    list_stair.append(int(sys.stdin.readline()))

if N <= 1:
    print(list_stair[0])
elif N <= 2:
    print(list_stair[0] + list_stair[1])
elif N <= 3:
    print(max(list_stair[0] + list_stair[2], list_stair[1] + list_stair[2]))
else:
    dp = [0] * N
    dp[0] = list_stair[0]
    dp[1] = list_stair[0] + list_stair[1]
    dp[2] = max(list_stair[0] + list_stair[2], list_stair[1] + list_stair[2])

    for i in range(3, N):
        dp[i] = max(
            dp[i - 2] + list_stair[i],
            dp[i - 3] + list_stair[i - 1] + list_stair[i]
        )
    # 천천히 점화식을 세워볼 것.
    print(dp[-1])
    # 최댓값을 출력하라