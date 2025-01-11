N, M = map(int, input().split())

set_1 = set()
result_set = set()

for i in range(N):
    set_1.add(input())
for i in range(M):
    temp = input()
    if temp in set_1:
        result_set.add(temp)

result_list = list(sorted(result_set))

print(len(result_list))
for item in result_list:
    print(item)
