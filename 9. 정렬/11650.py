N = int(input())

coordinates = list()

for i in range(N):
    coordinates.append(list(map(int, input().split())))

coordinates.sort()

for i in range(N):
    print(*coordinates[i])