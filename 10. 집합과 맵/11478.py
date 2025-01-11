S = input()

result_set = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        result_set.add(S[i:j + 1])

print(len(result_set))