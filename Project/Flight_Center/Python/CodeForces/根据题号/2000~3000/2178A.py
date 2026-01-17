for _ in range(int(input())):
    js = input()
    blacklist = 0
    for _ in js:
        if _ == 'Y':
            blacklist += 1
    if blacklist >= 2:
        print('NO')
    else:
        print('YES')
