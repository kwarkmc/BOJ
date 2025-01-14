T = int(input())

for i in range(T):
    stack = list()
    flag = False
    input_data = input()
    for item in input_data:
        if item == "(":
            stack.append(item)
        elif item == ")":
            if len(stack) > 0:
                stack.pop()
                flag = True
            else:
                flag = False
                break
    if len(stack) is not 0 or flag == False:
        print("NO")
    else:
        print("YES")

