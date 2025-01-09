M = int(input())
N = int(input())

lst = list()

for i in range(M, N + 1):
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                lst.append(i)
            break
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))
