string_list = list()

for _ in range(3):
    string_input = input()
    if string_input.isdigit():
        string_list.append(int(string_input))
    else:
        string_list.append(None)

for i in range(1, 3):
    if string_list[i - 1] is not None:
        string_list[i] = string_list[i - 1] + 1

string_next = string_list[2] + 1

if string_next % 3 == 0 and string_next % 5 == 0:
    print("FizzBuzz")
elif string_next % 3 == 0:
    print("Fizz")
elif string_next % 5 == 0:
    print("Buzz")
else:
    print(string_next)
