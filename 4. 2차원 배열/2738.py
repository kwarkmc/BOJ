N, M = map(int, input().split())
A = list()
B = list()
result = list()

for i in range(N):
	lst = list(map(int, input().split()))
	A.append(lst)

for i in range(N):
	lst = list(map(int, input().split()))
	B.append(lst)

for i in range(N):
	lst_temp = list()
	for j in range(M):
		lst_temp.append(A[i][j] + B[i][j])
	result.append(lst_temp)

for i in range(N):
	print(*result[i])
