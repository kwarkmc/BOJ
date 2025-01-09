N, B = map(int, input().split())

lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lst_temp = list(chr(i) for i in range(65, 91))
lst += lst_temp

s = ''

while N:
	s += str(lst[N % B])
	N //= B

print(s[::-1])