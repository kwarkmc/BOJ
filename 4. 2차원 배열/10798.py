lst = list()
max_len = 0
result = ""

for i in range(5):
	S = input()
	if len(S) > max_len:
		max_len = len(S)
	lst.append(S)

for i in range(max_len):
	for j in range(5):
		if len(lst[j]) <= i:
			continue
		result += lst[j][i]

print(result)

