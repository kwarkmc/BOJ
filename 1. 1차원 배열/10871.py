N, ans = map(int, input().split()) # 개수, 주어진 수

arr = list(map(int, input().split()))
result_arr = list()

for i in range(N):
	if arr[i] < ans:
		result_arr.append(arr[i])

print(*result_arr)