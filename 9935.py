import sys

# sys.stdin = open("input.txt", 'r')

string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []

for i in string:
    stack.append(i)
    # print(stack[len(stack) - len(bomb):len(stack)])
    if stack[len(stack) - len(bomb):len(stack)] == list(bomb):
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")