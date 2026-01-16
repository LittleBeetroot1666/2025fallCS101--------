def klnj(listy):
    return '\n'.join(listy)


def kpj(listy):
    return ' '.join(listy)


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


n = int(input())
js_0 = list(map(int, input().split()))
matt = permute0(js_0)
patt = []
for m in matt:
    if m not in patt:
        patt.append(m)
patt.sort()

for p in patt:
    ps = []
    for i in p:
        ps.append(str(i))
    print(kpj(ps))
