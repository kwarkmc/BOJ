dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

S = input()
result = 0

for i in S:
	for j in dial:
		if i in j:
			result += dial.index(j) + 3
print(result)