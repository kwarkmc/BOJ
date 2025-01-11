N = int(input())

log = set()

for i in range(N):
    name, isHere = map(str, input().split())
    if isHere == "enter":
        log.add(name)
    else:
        log.remove(name)

lst = sorted(log, reverse=True)

print(*lst)

