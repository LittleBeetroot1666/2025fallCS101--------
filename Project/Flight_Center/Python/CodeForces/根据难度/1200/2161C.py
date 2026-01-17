def kpj(listy):
    return ' '.join(listy)


Lne = int(input())
for _ in range(Lne):
    n, x = list(map(int, input().split()))
    js = list(map(int, input().split()))
    js.sort()
    jr = js.copy()
    jr.sort(reverse=True)
    i = 0
    j = 0
    init = 0
    res = []
    sgm = 0
    while i + j < n:
        if init + jr[j] < x:
            init += js[i]
            res.append(str(js[i]))
            i += 1

        else:
            init += jr[j]
            init -= x
            sgm += jr[j]
            res.append(str(jr[j]))
            j += 1

    print(sgm)
    print(kpj(res))