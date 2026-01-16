def subsets(listy):
    res0 = [[]]
    for i0 in listy:
        res0 += [r0 + [i0] for r0 in res0]
    return res0


def up(sest_001):
    blacklist_001 = 0
    if len(sest_001) == 1:
        return True
    else:
        for _ in range(len(sest_001) - 1):
            if sest_001[_] > sest_001[_ + 1]:
                blacklist_001 += 1
        if blacklist_001 == 0:
            return True
        else:
            return False


k = int(input())
js = list(map(int, input().split()))
ps = js[::-1]
r = 1

for ii in subsets(ps):
    if len(ii) >= 2 and up(ii) and len(ii) > r:
        r = len(ii)

print(r)
