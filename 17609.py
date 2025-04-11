import sys

# sys.stdin = open("input.txt", 'r')

T = int(sys.stdin.readline())   # 주어지는 문자열의 개수
for _ in range(T):
    string = list(sys.stdin.readline().rstrip())

    # 포인터 두개를 사용해 해결할 수 있다.
    result = 0
    left = 0
    right = len(string) - 1

    while left <= right:
        if result != 0:
            break

        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            temp1 = string[:left] + string[left + 1:]
            temp2 = string[:right] + string[right + 1:]
            if temp1 == temp1[::-1] or temp2 == temp2[::-1]:
                result = 1
            else:
                result = 2

    print(result)