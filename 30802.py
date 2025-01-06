N = int(input()) #전체 참가자의 수
shirt_size = list(map(int, input().split()))
T, P = map(int, input().split()) # T : 최소 주문해야 하는 티셔츠 묶음 수 , P : 최소 주문해야 하는 펜 묶음 수

result_shirt = 0
for i in shirt_size:
    result_shirt += i // T
    if i % T != 0:
        result_shirt += 1

print(result_shirt)
print(f"{N // P} {N % P}")