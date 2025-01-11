N = int(input())

numbers = list()

for i in range(N):
    numbers.append(int(input()))

numbers.sort()

for number in numbers:
    print(number)
