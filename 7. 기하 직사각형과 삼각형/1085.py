x, y, w, h = map(int, input().split())

print(min(x, y, w - x, h - y))

# result = 0
# if x < w or y < h:
#     result = (w - x) if (w - x) < (h - y) else (h - y)
# else:
#     result = ((x - w) ** 2 + (y - h) ** 2) ** 0.5
#
# print(result)
