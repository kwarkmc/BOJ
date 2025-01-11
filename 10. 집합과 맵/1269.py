A, B = map(int, input().split())

set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))
count = 0

for item in set_A:
    if item not in set_B:
        count += 1

for item in set_B:
    if item not in set_A:
        count += 1

print(count)