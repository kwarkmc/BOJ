N = int(input())

sum_1 = 0
sum_2 = 0

for i in range(1, N + 1):
	sum_1 += i
	sum_2 += i ** 3

print(sum_1)
print(sum_1 ** 2)
print(sum_2)
