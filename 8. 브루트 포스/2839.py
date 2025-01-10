N = int(input())

result = 2000
flag = False

for i in range(0, N // 5 + 1):
    for j in range(0, N // 3 + 1):
        temp = i * 5 + j * 3
        if temp == N:
            flag = True
            if (i + j) < 2000:
                result = i + j
if flag:
    print(result)
else:
    print(-1)