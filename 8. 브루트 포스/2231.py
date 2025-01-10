N = int(input())

result = 0
for M in range(1, N + 1):
    s = M + sum(int(digit) for digit in str(M))
    if s == N:
        result = M
        break
print(result)
