while True:
    n = int(input())
    if n == -1:
        break
    idx = 1
    string = f"{n} = 1"
    for i in range(2, n):
        if n % i == 0:
            idx += i
            string += f" + {i}"
    if idx == n:
        print(string)
    else:
        print(f"{n} is NOT perfect.")
