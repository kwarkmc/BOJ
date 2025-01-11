N, M = map(int, input().split())

S_set = set()
string_set = list()

for i in range(N):
    S_set.add(input())

for i in range(M):
    string_set.append(input())

count = 0

for i in string_set:
    if i in S_set:
        count += 1

print(count)