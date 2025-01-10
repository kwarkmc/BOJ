import sys, math

# sys.stdin = open("input.txt", "r")

def roundUp(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


N = int(sys.stdin.readline())

if N == 0:
    print(0)
else:
    list_input = list()

    for _ in range(N):
        list_input.append(int(sys.stdin.readline()))

    list_input.sort()
    to_remove = roundUp(N * 0.15)

    list_result = list_input[to_remove:N-to_remove]

    print(roundUp(sum(list_result) / len(list_result)))

'''
# O(n)으로 시도해보았으나 실패,, 다음번에 다시 도전해볼것
list_score = list([0] * 31)

for _ in range(N):
    i = int(sys.stdin.readline())
    list_score[i] += 1

to_remove_front = to_remove_back = math.ceil(N * 0.15)
index_front = 1
index_back = 30
final_number = N - (2 * to_remove_front)

for i in range(1, 31):
    if to_remove_front == 0:
        break
    if list_score[index_front] > 0:
        to_remove_front -= list_score[index_front]
        list_score[index_front] = 0
    index_front += 1

for i in range(1, 31):
    if to_remove_back == 0:
        break
    if list_score[index_back] > 0:
        to_remove_back -= list_score[index_back]
        list_score[index_back] = 0
    index_back -= 1
result = 0
for i in range(1, 31):
    result += i * list_score[i]
if final_number == 0:
    print(0)
else:
    print(round(result / final_number + 0.0000001))
'''
