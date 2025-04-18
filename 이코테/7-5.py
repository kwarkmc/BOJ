import sys

sys.stdin = open("input.txt", 'r')

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
array_stock = list(map(int, input().split()))

m = int(input())
array_req = list(map(int, input().split()))

array_stock.sort()

for i in array_req:
    result = binary_search(array_stock, i, 0, n - 1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')