# 바텀업 메모이제이션에서 사용되는 리스트는 DP 테이블이라고 부름.
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

# 바텀업 : 작은 문제부터 차근차근 답을 도출한다.
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])