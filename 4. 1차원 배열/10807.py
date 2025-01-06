N = int(input())
arr = list(map(int, input().split()))
ans = int(input())
result = 0

for i in range(N):
	if arr[i] == ans:
		result += 1

print(result)
# print(arr.count(ans))