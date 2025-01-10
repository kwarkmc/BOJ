lst = list()

for _ in range(3):
    lst.append(int(input()))

# if sum(lst) is not 180:
#     print("Error")
# else:
#     if lst[0] == lst[1] or lst[0] == lst[2] or lst[1] == lst[2]:
#         if lst[0] == lst[1] == lst[2]:
#             print("Equilateral")
#         else:
#             print("Isosceles")
#     else:
#         print("Scalene")

if lst.count(60) == 3:
    print("Equilateral")
elif sum(lst) == 180 and len(set(lst)) == 2:
    print("Isosceles")
elif sum(lst) == 180 and len(set(lst)) == 3:
    print("Scalene")
else:
    print("Error")



