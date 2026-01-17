def kpj(listy):
    return ' '.join(listy)


def to_str(listy):
    lististr = []
    for i_in_listy in listy:
        lististr.append(str(i_in_listy))
    return lististr


Lne = int(input())
for _ in range(Lne):
    n = int(input())
    js = list(map(int, input().split()))
    pl = [j % 2 for j in js]
    sg = sum(pl)
    if sg == 0 or sg == n:
        jsi = to_str(js)
        print(kpj(jsi))
    else:
        js.sort()
        jsi = to_str(js)
        print(kpj(jsi))
