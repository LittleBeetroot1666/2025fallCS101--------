for _ in range(int(input())):
    l, r, x = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    if a == b:
        print(0)
    elif (a - l < x and r - a < x) or (b - l < x and r - b < x):
        print(-1)
    elif abs(a - b) >= x:
        print(1)
    else:
        if (a - l >= x and b - l >= x) or (r - a >= x and r - b >= x):
            print(2)
        else:
            print(3)
