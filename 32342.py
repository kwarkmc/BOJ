N = int(input())

for i in range(N):
    string = input()
    count = 0
    for j in range(len(string)):
        if string[j : j + 3] == "WOW":
            count += 1
    print(count)