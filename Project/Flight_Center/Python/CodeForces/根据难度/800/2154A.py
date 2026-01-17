for _ in range(int(input())):
    n, k = map(int, input().split())
    st = input()
    cnt = 0
    i = 0
    bl = 0
    z = k
    while i <= n - 1:
        if st[i] == '0':
            z += 1
            i = i + 1
        elif st[i] == '1':
            if z >= k - 1:
                cnt += 1
                z = 0
                i = i + 1
            else:
                z = 0
                i = i + 1
    print(cnt)
