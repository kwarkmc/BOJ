arr = list()

for i in range(9):
	A = int(input())
	arr.append(A)

print(max(arr))
print(arr.index(max(arr)) + 1)