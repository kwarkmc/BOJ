N, B = map(str, input().split())

B_int = int(B)

lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lst_temp = list(chr(i) for i in range(65, 91))
lst += lst_temp

N = N[::-1]

result = lst.index(N[0])

for i in range(1, len(N)):
	result += lst.index(N[i]) * (B_int ** i)
	
print(result)