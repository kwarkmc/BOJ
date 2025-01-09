N = int(input())

lst = [25, 10, 5, 1]

for i in range(N):
	lst_temp = list()
	C = int(input())
	for j in lst:
		x = C // j
		C = C % j
		lst_temp.append(x)
	print(*lst_temp)