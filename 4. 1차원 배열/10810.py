N, count = map(int, input().split())
arr = list(0 for i in range(N))

for a in range(count):
	i, j, k = map(int, input().split())
	for b in range(i, j + 1):
		arr[b - 1] = k

print(*arr)