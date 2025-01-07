N = int(input())
group_word = N

for i in range(N):
	S = input()
	for j in range(len(S) - 1):
		if S[j] == S[j+1]:
			continue
		elif S[j] in S[j+1:]:
			group_word += -1
			break
print(group_word)

