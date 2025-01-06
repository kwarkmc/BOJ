ans = 0

while True:
	try:
		N = input()
		ans += 1
	except EOFError:
		break

print(ans)