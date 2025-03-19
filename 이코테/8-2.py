'''
DP (Dynamic Programming)
메모이제이션 (Memoization), 캐싱 (Caching)
1. 큰 문제는 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 답은 그것을 포함하는 큰 문제에서 동일하다
-> 구한 정보는 리스트에 저장했다가 같은 정보가 필요할 때 그대로 리스트에서 가져온다.
'''

# 한 번 계산된 결과를 메모이제이션 하기 위한 리스트
d = [0] * 100

# 탑다운 다이나믹 프로그래밍
def fibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 계산한 적 없는 문제라면 점화식에 따라 계산
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(6))