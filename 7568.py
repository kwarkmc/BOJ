# import sys
#
# sys.stdin = open("input.txt", "r")

N = int(input())

list_input = list()
list_ans = list()
for _ in range(N):
    x, y = map(int, input().split())
    list_input.append([x, y])

for i in list_input:
    count = 0
    for j in list_input:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1
    list_ans.append(count + 1)

print(*list_ans)