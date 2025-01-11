numbers = list()

for i in range(5):
    numbers.append(int(input()))

numbers.sort()

print(sum(numbers) // len(numbers))
print(numbers[len(numbers) // 2])
