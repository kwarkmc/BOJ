import sys

# sys.stdin = open("input.txt", "r")

seq_0 = [1, 0, 1]   # fib(0), fib(1), fib(2)
seq_1 = [0, 1, 1]   # fib(0), fib(1), fib(2)


def fib(x):
    if x >= len(seq_0):
        for i in range(len(seq_0), x + 1):
            seq_0.append(seq_0[i - 1] + seq_0[i - 2])
            seq_1.append(seq_1[i - 1] + seq_1[i - 2])
    print(f'{seq_0[x]} {seq_1[x]}')


T = int(sys.stdin.readline())

for _ in range(T):
    x = int(sys.stdin.readline())
    fib(x)
