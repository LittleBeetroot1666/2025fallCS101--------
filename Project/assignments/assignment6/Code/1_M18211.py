# Python,two pointers,greedy
p = int(input())
js = list(map(int, input().split()))
js.sort()
jsr = []
for _ in range(1,len(js)+1):
    jsr.append(js[-_])

lt = len(js)
if p < js[0]:
    print(0)
else:
    a = b = 0
    a += 1
    p -= js[0]
    dta = 1
    while a + b < lt:
        while p >= js[a]:
            p -= js[a]
            a += 1
            dta += 1
        if jsr[b] >= js[a]:
            p += jsr[b] - js[a]
            a += 1
            b += 1

    print(dta)
