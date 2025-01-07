lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

S = input()
count = 0

for item in lst:
	# S[a:a + len(item)] = 'A'
	S = S.replace(item, "A")
print(len(S))
