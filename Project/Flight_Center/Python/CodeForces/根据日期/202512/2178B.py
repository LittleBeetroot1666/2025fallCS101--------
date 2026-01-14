for _ in range(int(input())):
    js = input()
    cnt = 0
    blacklist = 1
    for _ in js:
        if _ == 's':
            blacklist = 0
        if _ == 'u':
            if blacklist == 0:
                blacklist += 1
            else:
                blacklist = 0
                cnt += 1
    print(cnt + blacklist)
