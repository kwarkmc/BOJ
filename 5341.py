while True:
    N = int(input())
    if N == 0:
        break
    total = 0
    for i in range(N, 0, -1):
        total += i
    print(total)