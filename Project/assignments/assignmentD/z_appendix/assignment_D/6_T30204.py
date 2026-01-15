n, m = list(map(int, input().split()))
min_circ = float('inf')
birds = []
asq = []
for _ in range(n):
    i, j = list(map(int, input().split()))
    birds.append(i)
    if i + j < min_circ:
        min_circ = i + j
        asq.append(max(i, j))

early_birds = []
late_birds = [asq[-1]]
for i in birds:
    if i <= min_circ // 2:
        early_birds.append(i)
    elif min_circ // 2 < i <= asq[-1]:
        late_birds.append(i)
early_birds.sort()
late_birds.sort()

cnt = 0
sgm = 0
s0 = sum(early_birds)
l0 = len(early_birds)
if m == s0:
    print(l0)
elif m < s0:
    init_eb = 0
    while sgm <= m - early_birds[init_eb]:
        sgm += early_birds[init_eb]
        init_eb += 1
    print(init_eb)
else:
    m -= s0
    cnt += l0
    cnt += 2 * m // min_circ
    m = m % min_circ
    print(cnt)

