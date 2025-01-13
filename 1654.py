import sys

# sys.stdin = open("input.txt", "r")

K, N = map(int, sys.stdin.readline().split())

list_cord = [0] * K

for i in range(K):
    list_cord[i] = int(sys.stdin.readline())

high = max(list_cord)   # 이분탐색을 시작할 때 사용되는 가장 높은 high
res = 0

def binary(low, high):
    if high < low:
        return
    global N
    global res

    mid = (low + high) // 2
    temp = 0
    for i in list_cord:
        temp += i // mid    # list_cord에 있는 주어진 랜선의 길이를 mid 값으로 나눠보고, 만들 수 있는 선의 개수를 구한다 -> temp
    if temp >= N:
        res = mid
        binary(mid + 1, high)
    else:
        binary(low, mid - 1)


binary(1, high)
print(res)