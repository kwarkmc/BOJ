while True:
    input_data = input()
    if input_data == ".":
        break
    stack = list()
    for item in input_data:
        if item == "(" or item == "[":
            stack.append(item)
        elif item == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(item)
        elif item == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(item)
    if len(stack) == 0:
        print("yes")
    else:
        print("no")