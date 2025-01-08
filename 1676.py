import math

N = int(input())

result = str(math.factorial(N))

result = result[::-1]

count = 0
for i in result:
    if i == '0':
        count += 1
    else:
        break

print(count)