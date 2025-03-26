import sys

# sys.stdin = open('input.txt', 'r')

K = int(sys.stdin.readline())   # 테스트 케이스의 수

triangle = [n * (n + 1) // 2 for n in range(1, 46)] # 45번째 삼각수가 1035임.
array = [0] * 1001

# 미리 1000개의 숫자에 대해 삼각수로 계산되는지 array[num] = 1로 표시한다.
for i in triangle:
    for j in triangle:
        for k in triangle:
            num = i + j + k
            if num <= 1000:
                array[num] = 1

for _ in range(K):
    num = int(sys.stdin.readline())
    print(array[num])