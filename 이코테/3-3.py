N, M = map(int, input().split())    # N -> 행, M -> 열

result = 0

for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
