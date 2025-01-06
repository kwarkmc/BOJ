N, M = map(int, input().split())

arr = list(i + 1 for i in range(N))
temp = 0

for a in range(M):
	i, j = map(int, input().split())
	temp = arr[i-1:j]
	temp.reverse()
	arr[i-1:j] = temp
	
print(*arr)