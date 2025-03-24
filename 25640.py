import sys

sys.stdin = open('input.txt', 'r')

jinho = sys.stdin.readline()
N = int(sys.stdin.readline())
count = 0

for _ in range(N):
    input_MBTI = sys.stdin.readline()
    if input_MBTI == jinho:
        count += 1

print(count)