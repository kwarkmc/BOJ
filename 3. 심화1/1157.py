# from collections import Counter

# S = input().upper()

# counts = Counter(S)

# most_common = counts.most_common()

# max_count = most_common[0][1]
# result = most_common[0][0]

# if sum(1 for item in most_common if item[1] == max_count) > 1:
# 	print("?")
# else:
# 	print(result)

S = input().upper()
S_list = list(set(S))
lst = []

for i in S_list:
	count = S.count(i)
	lst.append(count)

if lst.count(max(lst)) >= 2:
	print("?")
else:
	print(S_list[lst.index(max(lst))])