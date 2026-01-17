Lne = int(input())
for _ in range(Lne):
    r0, x, d, n = list(map(int, input().split()))
    js = str(input())
    cnt = 0
    for i in range(len(js)):
        if js[i] == '1':
            r0 -= min(r0, d)
            cnt += 1
        else:
            if r0 < x:
                r0 -= min(r0, d)
                cnt += 1
    print(cnt)
