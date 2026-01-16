def k0j(listy):
    return ''.join(listy)


def _2sqr(x0, y0, x1, y1):
    if abs(x0 - x1) == abs(y0 - y1):
        return True
    else:
        return False


def permute0(listy):
    if len(listy) == 1:
        return [[listy[0]]]
    else:
        al_listy = []
        for j_in_listy in listy:
            n_listy = [j_in_listy]
            listy0 = listy[:]
            listy0.remove(j_in_listy)
            for k_in_listyf in permute0(listy0):
                for k_in_listy in k_in_listyf:
                    n_listy.append(k_in_listy)
                al_listy.append(n_listy)
                n_listy = [j_in_listy]
        return al_listy


al = permute0([1, 2, 3, 4, 5, 6, 7, 8])
bl = []
for a in al:
    blacklist = 0
    for i in range(0, 7):
        if blacklist == 0:
            for j in range(i + 1, 8):
                if _2sqr(i + 1, int(a[i]), j + 1, int(a[j])):
                    blacklist = 1
                    break

    if blacklist == 0:
        bl.append(a)


res = []
for a in bl:
    aa = []
    for b in a:
        aa.append(str(b))
    res.append(aa)
res.sort()

Lne = int(input())
for _ in range(Lne):
    n = int(input())
    print(k0j(res[n - 1]))
