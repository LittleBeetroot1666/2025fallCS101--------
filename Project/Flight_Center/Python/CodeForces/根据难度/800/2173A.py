for _ in range(int(input())):
    n, k = map(int, input().split())
    js = input()
    sg0 = 0
    cnt = 0
    for j in js:
        if j == '0':
            if sg0 == 0:
                cnt += 1
            else:
                sg0 -= 1
        else:
            sg0 = k
    print(cnt)
