N = int(input())
list_input = list(map(int, input().split()))

d = [0] * 100
d[0] = list_input[0]
d[1] = max(list_input[0], list_input[1])

for i in range(2, N):
    d[i] = max(d[i - 1], d[i - 2] + list_input[i])

print(d[N - 1])