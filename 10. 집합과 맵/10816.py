from collections import Counter

N = int(input())

lst = list(map(int, input().split()))

M = int(input())

lst_result = list(map(int, input().split()))

count_dict = Counter(lst)

for item in lst_result:
    print(count_dict.get(item, 0), end=' ')