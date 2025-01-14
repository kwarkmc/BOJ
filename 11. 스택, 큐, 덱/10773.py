K = int(input())

stack = list()

for i in range(K):
    input_data = int(input())
    if input_data == 0:
        stack.pop()
    else:
        stack.append(input_data)

print(sum(stack))