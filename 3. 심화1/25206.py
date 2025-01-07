lst = ['F', '', 'D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']

total_point = 0
total = 0
avg = 0

for i in range(1, 21):
	name, point, score = map(str, input().split())
	if score == "P":
		continue
	total_point += float(point)
	score_float = lst.index(score) * 0.5
	total += float(point) * score_float
avg = total / total_point
print(avg)