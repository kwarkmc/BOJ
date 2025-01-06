arr = []
for i in range(10):
	arr.append(int(input()) % 42)

# arr = [int(input()) for i in range(10)]

arr = set(arr)
print(len(arr))

# 다른 풀이

arr = []

for i in range(10):
	num = int(input())
	if num % 42 not in arr:
		arr.append(num % 42)
print(len(arr))

