def calc(n):
    array = str(n)
    result = 0
    for i in array:
        result += int(i) ** 2
    return result

n = int(input())

while 1:
    n = calc(n)
    if n == 4:
        print('UNHAPPY')
        break
    elif n == 1:
        print('HAPPY')
        break
