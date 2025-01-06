N = int(input())

for _ in range(N):
    string = input()
    stack = list()
    score = 0
    for i in string:
        if i == "O":
            stack.append(1)
            score += len(stack)
        elif i == "X":
            stack = []
    print(score)

