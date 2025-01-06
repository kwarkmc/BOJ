L = int(input())

for i in range(L):
    N, S = map(str, input().split())
    print(S * int(N))
