blacklist = 0
while blacklist == 0:
    n, m = list(map(int, input().split()))
    if m + n >= 1:
        otto = []
        cnt = 0
        o = 0
        for i in range(1, n + 1):
            otto.append(i)
        while len(otto) > 1:
            cnt += 1
            o += 1
            if cnt == m:
                cnt = 0
                ot = (o - 1) % len(otto)
                otto.remove(otto[ot])
                o = ot
        print(*otto)
    else:
        blacklist = 1
        break
