def setm(monk, seat):
    if monk >= seat:
        return 0
    else:
        return seat - monk


for _ in range(int(input())):
    m, a, b, c = list(map(int, input().split()))
    m1 = m
    m2 = m
    re = 0
    re += setm(a, m)
    re += setm(b, m)
    re1 = setm(c, re)
    res = 2 * m - re1
    print(res)
