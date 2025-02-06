# a = 97

string = input()

row = int(string[1])
column = ord(string[0]) - 96

moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

count = 0

for move in moves:
    nrow = row + move[0]
    ncolumn = column + move[1]
    if nrow > 8 or nrow < 1 or ncolumn > 8 or ncolumn < 1:
        continue
    else:
        count += 1

print(count)