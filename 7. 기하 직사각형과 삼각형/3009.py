lst_x = list()
lst_y = list()

for i in range(3):
    A, B = map(int, input().split())
    if A in lst_x:
        lst_x.remove(A)
    else:
        lst_x.append(A)
    if B in lst_y:
        lst_y.remove(B)
    else:
        lst_y.append(B)

print(*lst_x, *lst_y)
