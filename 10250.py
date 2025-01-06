case = int(input())

for _ in range(1, case + 1):
    H, W, N = map(int, input().split()) #H X W 건물, N 번째 손님
    N = N - 1
    a = N // H #a:1
    b = N % H #b=4


    print(f"{b + 1}{a + 1:02}")