N, M = map(int, input().split())

lst = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            s = lst[i] + lst[j] + lst[k]
            if M >= s > result:
                result = s
print(result)