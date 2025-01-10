N = int(input())
# min_x = 10000
# min_y = 10000
# max_x = -10000
# max_y = -10000
#
# for i in range(N):
#     x, y = map(int, input().split())
#     if min_x > x:
#         min_x = x
#     if min_y > y:
#         min_y = y
#     if max_x < x:
#         max_x = x
#     if max_y < y:
#         max_y = y
# if N <= 1:
#     print(0)
# else:
#     print((max_x - min_x) * (max_y - min_y))

x_lst = list()
y_lst = list()
for i in range(N):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
print((max(x_lst) - min(x_lst)) * (max(y_lst) - min(y_lst)))