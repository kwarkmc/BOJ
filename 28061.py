N = int(input())

lst = list(map(int, input().split()))

lemon = [lst[i] - (N - i) for i in range(N)]

print(max(lemon))
