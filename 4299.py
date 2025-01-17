A, B = map(int, input().split())

if (A + B) % 2 != 0 or (A + B) < 0 or (A - B) < 0:  # A + B < 0 인 경우는 x가 음수, A - B < 0 인 경우는 y가 음수
    print(-1)
else:
    X = (A + B) // 2
    Y = A - X
    print(f"{X} {Y}")