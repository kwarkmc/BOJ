N = int(input())

stack_input = list(map(int, input().split()))
stack_input.reverse()
stack_waitline = list()

idx = 1

while len(stack_input) > 0:
    if stack_input[-1] == idx:
        stack_input.pop()
        idx += 1
    else:
        if len(stack_waitline) > 0 and stack_waitline[-1] == idx:
            stack_waitline.pop()
            idx += 1
        else:
            stack_waitline.append(stack_input.pop())

while len(stack_waitline) > 0:
    if stack_waitline[-1] == idx:
        stack_waitline.pop()
        idx += 1
    else:
        break

if idx == N + 1:
    print("Nice")
else:
    print("Sad")