N = int(input())

coordinates = list()

for i in range(N):
    coordinates.append(list(map(int, input().split())))

coordinates.sort(key= lambda x: (x[1], x[0]))

for i in range(N):
    print(*coordinates[i])