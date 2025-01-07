max_num = 0
max_position = [1, 1]

for i in range(9):
	row = list(map(int, input().split()))
	if max(row) > max_num:
		max_num = max(row)
		max_position = [i + 1, row.index(max(row)) + 1]

print(max_num)
print(*max_position)