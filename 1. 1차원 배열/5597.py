list_org = list(i + 1 for i in range(30))
list_input = list()

for i in range(28):
	A = int(input())
	list_input.append(A)

for i in list_org:
	if i not in list_input:
		print(i)