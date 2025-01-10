while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    lst = [a, b, c]
    lst.sort()
    if (lst[0] + lst[1]) <= lst[2]:
        print("Invalid")
    elif len(set(lst)) == 1:
        print("Equilateral")
    elif len(set(lst)) == 2:
        print("Isosceles")
    else:
        print("Scalene")