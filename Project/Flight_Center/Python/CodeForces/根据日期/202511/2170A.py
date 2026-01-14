for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(9)
    elif n == 3:
        print(29)
    elif n == 4:
        print(56)
    else:
        print(5 * (n * (n - 1) - 1))
    