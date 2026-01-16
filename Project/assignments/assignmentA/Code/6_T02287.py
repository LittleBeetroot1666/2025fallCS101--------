while True:
    n = int(input())
    if n == 0:
        break

    tj = list(map(int, input().split()))
    tj.sort()
    gw = list(map(int, input().split()))
    gw.sort()

    lt = 0
    rt = n - 1
    lg = 0
    rg = n - 1
    cnt = 0
    while lt <= rt:
        if tj[lt] > gw[lg]:
            cnt += 1
            lt += 1
            lg += 1
        elif tj[rt] > gw[rg]:
            cnt += 1
            rt -= 1
            rg -= 1
        else:
            if tj[lt] < gw[rg]:
                cnt -= 1

            lt += 1
            rg -= 1

    print(200 * cnt)
