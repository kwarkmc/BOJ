N = int(input())

a = 2
b = 1

for i in range(N):
	a += b
	b *= 2

print(a ** 2)