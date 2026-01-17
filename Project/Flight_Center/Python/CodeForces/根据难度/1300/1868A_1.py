def to_listie(n_to_listie):
    return [i_to_listie for i_to_listie in range(n_to_listie)]


def str_to_listie(n_to_listie):
    return [str(i_to_listie) for i_to_listie in range(n_to_listie)]


def cata_findm(n0, m0):
    if m0 == 1:
        return 0
    else:
        return min(n0 + 1, m0)


def alter_listie(listy):
    first = listy.pop(0)
    listy.append(first)
    return listy


def kpj(strry_listy):
    return ' '.join(strry_listy)


Lne = int(input())
for _l in range(Lne):
    n, m = list(map(int, input().split()))
    print(cata_findm(n, m))
    if m == 1:
        for _ in range(n):
            print(0)
    else:
        genlistie = str_to_listie(m)
        ltt = str_to_listie(m)
        cnt = 1
        while cnt <= min(m - 1, n):
            print(kpj(ltt))
            cnt += 1
            ltt = alter_listie(ltt)
        if m - 1 < n:
            for _ in range(n - m + 1):
                print(kpj(genlistie))
