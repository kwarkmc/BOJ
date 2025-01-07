N = int(input())

R = 2 * N - 1

for i in range(1, R + 1):
	print(" " * (R - i // 2) + "*" * (i * 2 - 1) + " " * (R - i // 2))