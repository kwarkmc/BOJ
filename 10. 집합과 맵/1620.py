import sys

def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

poke_dict = dict()
reverse_poke_dict = dict()

for i in range(1, N + 1):
    name = input()
    poke_dict[i] = name
    reverse_poke_dict[name] = i

for j in range(M):
    question = input()
    if question.isdigit():
        print(poke_dict[int(question)])
    else:
        print(reverse_poke_dict[question])
