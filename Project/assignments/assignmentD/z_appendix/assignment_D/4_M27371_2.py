def k0j(listy):
    return ''.join(listy)


key = input()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
         'x', 'y', 'z']
kg = []
sl = {}
itt = 0
ress = []
for ki in key:
    if ki == 'j' and 'i' not in sl:
        sl['i'] = [itt // 5, itt % 5]
        kg.append('i')
        itt += 1
    elif ki not in sl:
        sl[ki] = [itt // 5, itt % 5]
        kg.append(ki)
        itt += 1
for ai in alpha:
    if ai not in sl:
        sl[ai] = [itt // 5, itt % 5]
        kg.append(ai)
        itt += 1

for _ in range(int(input())):
    tara = input()
    res = []
    tof = len(tara)
    itig = 0
    while itig < tof - 1:
        if tara[itig] != tara[itig + 1]:
            a = tara[itig]
            b = tara[itig + 1]
            itig += 2
        else:
            if tara[itig] == 'x':
                a = tara[itig]
                b = 'q'
                itig += 1
            else:
                a = tara[itig]
                b = 'x'
                itig += 1

        if a == 'j':
            a = 'i'
        if b == 'j':
            b = 'i'

        if sl[a][0] == sl[b][0]:
            res.append(kg[(sl[a][0] * 5 + (sl[a][1] + 1) % 5) % 25])
            res.append(kg[(sl[b][0] * 5 + (sl[b][1] + 1) % 5) % 25])
        elif sl[a][1] == sl[b][1]:
            res.append(kg[((sl[a][0] + 1) % 5 * 5 + sl[a][1]) % 25])
            res.append(kg[((sl[b][0] + 1) % 5 * 5 + sl[b][1]) % 25])
        else:
            res.append(kg[(sl[a][0] * 5 + sl[b][1]) % 25])
            res.append(kg[(sl[b][0] * 5 + sl[a][1]) % 25])

    if itig == tof - 1:
        a = tara[itig]
        if a == 'x':
            b = 'q'
        else:
            b = 'x'

        if sl[a][0] == sl[b][0]:
            res.append(kg[(sl[a][0] * 5 + (sl[a][1] + 1) % 5) % 25])
            res.append(kg[(sl[b][0] * 5 + (sl[b][1] + 1) % 5) % 25])
        elif sl[a][1] == sl[b][1]:
            res.append(kg[((sl[a][0] + 1) % 5 * 5 + sl[a][1]) % 25])
            res.append(kg[((sl[b][0] + 1) % 5 * 5 + sl[b][1]) % 25])
        else:
            res.append(kg[(sl[a][0] * 5 + sl[b][1]) % 25])
            res.append(kg[(sl[b][0] * 5 + sl[a][1]) % 25])

    ress.append(k0j(res))

for res in ress:
    print(res)
