import sys

# sys.stdin = open("input.txt", 'r')

answer = 0

input_str = sys.stdin.readline()

input_minus = input_str.split('-')

result = sum(map(int, (input_minus[0].split('+'))))
if input_str[0] == '-':
    answer -= result
else:
    answer += result

for x in input_minus[1:]:
    x = sum(map(int, (x.split('+'))))
    answer -= x

print(answer)