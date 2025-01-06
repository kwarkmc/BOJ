#
# print(ord('X'))
# print(ord('Y'))
# print(ord('Z'))
# print(ord('A'))
# print(ord('B'))
# print(ord('C'))
# print(chr(65))

string = input()

result = ""

for i in range(len(string)):
    changed = 0
    if string[i] in ['A', 'B', 'C']:
        changed = ord(string[i]) + 23
    else:
        changed = ord(string[i]) - 3
    result += chr(changed)

print(result)