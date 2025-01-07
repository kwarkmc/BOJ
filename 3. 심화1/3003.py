org = [1, 1, 2, 2, 2, 8]
result = list()

S = list(map(int, input().split()))

for i in range(len(org)):
	result.append(org[i] - S[i])

print(*result)