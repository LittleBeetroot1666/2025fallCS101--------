n = 1
while n != 0:
    n = int(input())
    if n == 0:
        break
    else:
        s = []
        for i in range(0, n):
            u, t = list(map(int, input().split()))
            v = u / 3.6
            if t >= 0:
                k = 4500 / v + t
                kk = round(k + 0.2)
                s.append(kk)
    print(min(s))
