blacklist = 0
while blacklist == 0:
    n, p, m = list(map(int, input().split()))
    if m + n + p >= 1:
        otto = []
        cnt = 0
        o = p - 1
        shuodedaoli = []
        for i in range(1, n + 1):
            otto.append(i)
        while len(otto) > 1:
            cnt += 1
            o += 1
            if cnt == m:
                cnt = 0
                ot = (o - 1) % len(otto)
                shuodedaoli.append(otto[ot])
                otto.remove(otto[ot])
                o = ot
        shuodedaoli.append(otto[0])
        print(','.join(map(str, shuodedaoli)))
    else:
        blacklist = 1
        break
