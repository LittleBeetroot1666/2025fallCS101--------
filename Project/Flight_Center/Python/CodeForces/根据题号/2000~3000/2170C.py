for _ in range(int(input())):
    inti = 0
    intj = 0
    cnt = 0
    n, k = list(map(int, input().split()))
    qs = list(map(int, input().split()))
    qs.sort()
    rs = list(map(int, input().split()))
    rs.sort(reverse=True)
    while intj <= n - 1:
        if k >= (rs[intj] + 1) * qs[inti] + rs[intj]:
            inti += 1
            intj += 1
            cnt += 1
        else:
            intj += 1

    print(cnt)
