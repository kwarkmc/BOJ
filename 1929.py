import sys, math

# 이중 For 문을 사용해 M ~ N 에 대해 모두 브루트포스로 소수인지 확인하면 O(N^2) 나와서 TimeOut.
# 약수의 성질을 이용해 O(N^3/2)로 개선했다.

# 약수의 성질 -> 모든 약수는 가운데 약수를 기준으로 대칭을 이룬다. : 특정한 자연수의 약수를 찾을 때 가운데 약수 (제곱근)까지만 확인하면 된다.
# O(N) -> O(N^1/2)

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):   # 2부터 x의 제곱근까지 모든 수를 순회하며
        if x % i == 0:  # x가 해당 수로 나누어 떨어진다면 소수가 아님.
            return False
    return True

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N + 1):
    if i == 1:
        pass
    elif is_prime_number(i):
        print(i)