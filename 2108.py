import sys
from collections import Counter

# sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
list_input = list()

for _ in range(N):
    list_input.append(int(sys.stdin.readline()))

list_input.sort()

print(round(sum(list_input) / len(list_input)))    # 산술평균
print(list_input[len(list_input) // 2]) # 중앙값
counts = Counter(list_input)
common = counts.most_common()

max_freq = common[0][1]
candidates = [value for value, freq in common if freq == max_freq]  # 리스트 컴프리헨션
if len(candidates) > 1:
    print(sorted(candidates)[1])
else:
    print(candidates[0])
# 최빈값 -> 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
print(list_input[-1] - list_input[0])    # 범위