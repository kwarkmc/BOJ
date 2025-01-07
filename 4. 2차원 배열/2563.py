lst = list([0] * 100 for i in range(100))

N = int(input())

for i in range(N):
	x, y = map(int, input().split())
	for a in range(10):
		for b in range(10):
			lst[x + a][y + b] = 1

result = 0
for i in range(100):
	result += sum(lst[i])

print(result)
#FOR TEST#
# for i in range(100):
# 	for j in range(100):
# 		print(lst[i][j], end="")
# 	print()
