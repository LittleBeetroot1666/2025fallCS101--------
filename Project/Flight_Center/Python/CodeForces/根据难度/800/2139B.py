for i in range(int(input())):
    n, m = list(map(int, input().split()))
    js = list(map(int, input().split()))
    js.sort()
    a = []
    s = 0
    for j in range(0, n):
        a.append(js[j])
    while n > 0 and m > 0:
        s += m*a[n-1]
        n -= 1
        m -= 1
    print(s)
