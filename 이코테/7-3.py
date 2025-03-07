# 반복문을 사용한 이진탐색

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        # 찾은 경우 중간 값 리턴
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값 보다 찾고자 하는 값이 더 작을 경우 배열 왼쪽 탐색
        else:
            start = mid + 1
        # 중간점의 값보다 찾고자 하는 값이 더 클 경우 배열 오른쪽 탐색
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)