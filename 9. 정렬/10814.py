N = int(input())

lst = list()

for _ in range(N):
    age, name = map(str, input().split())
    lst.append((int(age), name))

lst.sort(key= lambda x: x[0])

for item in lst:
    print(*item)