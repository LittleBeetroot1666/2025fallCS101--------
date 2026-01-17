for i in range(int(input())):
    s = 0
    a, b = list(map(int, input().split()))
    if a % b != 0:
        s = b - a % b
    print(s)
