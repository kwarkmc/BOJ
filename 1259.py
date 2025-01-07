while True:
    string = input()
    if string == '0':
        break
    stack = list()
    res = ''
    for i in string:
        stack.append(i)
    for i in range(len(stack)):
        res += stack.pop()
    if res == string:
        print('yes')
    else:
        print('no')
