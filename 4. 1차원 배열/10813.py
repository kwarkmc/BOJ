N, M = map(int, input().split())

arr = list(i + 1 for i in range(N))

for i in range(M):
	A, B = map(int, input().split())
	# temp = arr[A - 1]
	# arr[A - 1] = arr[B - 1]
	# arr[B - 1] = temp
	arr[A - 1], arr[B - 1] = arr[B - 1], arr[A - 1]

print(*arr)