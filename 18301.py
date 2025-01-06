import math

a, b, c = map(int, input().split())

temp = (a + 1) * (b + 1) / (c + 1) - 1

print(math.floor(temp))