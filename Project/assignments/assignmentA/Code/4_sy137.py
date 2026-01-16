def kpj(listy):
    return ' '.join(listy)


def subsets(listy):
    res0 = [[]]
    for i0 in listy:
        res0 += [r0 + [i0] for r0 in res0]  # 每个元素扩展当前所有子集
    return res0


n, k = list(map(int, input().split()))
js = list(map(int, input().split()))

ress = []
for j in subsets(js):
    if len(j) == k:
        ress.append(j)
ress.sort()
resr = []
for r1 in ress:
    if r1 not in resr:
        resr.append(r1)

ps = []
for r2 in resr:
    ps.append([str(i) for i in r2])

for r3 in ps:
    print(kpj(r3))
