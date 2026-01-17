for _ in range(int(input())):
    stt = input()
    if len(stt) == 1:
        print(1)
    elif '>*' in stt or '**' in stt or '*<' in stt or '><' in stt:
        print(-1)
    else:
        l = 0
        r = 0
        if '*' in stt:
            l += 1
            r += 1
        for t0 in stt:
            if t0 == '<':
                l += 1
            elif t0 == '>':
                r += 1
        print(max(l, r))
