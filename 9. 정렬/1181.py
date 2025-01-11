N = int(input())

lst = list()

for i in range(N):
    lst.append(input())

lst = list(set(lst))

lst.sort(key= lambda x: (len(x), x))

for item in lst:
    print(item)