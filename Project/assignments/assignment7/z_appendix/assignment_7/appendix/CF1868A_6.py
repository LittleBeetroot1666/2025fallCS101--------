t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    if m == 1:
        for _ in range(n + 1):
            print(0)
    elif n == 1:
        js = [str(i) for i in range(m)]
        print(2)
        print(*js)
    else:
        print(min(n + 1, m))
        js = [str(i) for i in range(m)]
        for j in range(0, min(n, m) - 1):
            js.remove(str(j))
            js.append(str(j))
            print(*js)
        if n >= m:
            for i in range(n - m + 1):
                print(*js)
