'''N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
data.reverse()
first = data[0]
second = data[1]

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)
'''

N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[N - 1]
second = data[N - 2]

count = int(M / (K + 1)) * K
count += M % (K + 1)

result = 0
result += count * first
result += (M - count) * second

print(result)
