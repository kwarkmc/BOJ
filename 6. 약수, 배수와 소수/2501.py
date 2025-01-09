N, K = map(int, input().split())

idx = 0
isPrint = False

for i in range(1, N):
    if N % i == 0:
        idx += 1
        if idx == K:
            print(i)
            isPrint = True
            break
if isPrint == False:
    print(0)