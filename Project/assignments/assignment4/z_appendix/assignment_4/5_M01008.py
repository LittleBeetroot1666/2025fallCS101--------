n = int(input())
print(n)
for i in range(n):
    a, b, c = list(map(str, input().split()))
    month1 = [m.strip() for m in "pop, no, zip, zotz, tzec, xul, yoxkin, mol, chen, yax, zac, ceh, mac, kankin, muan, pax, koyab, cumhu, uayet".split(',')]
    chk1 = {m: i for i, m in enumerate(month1)}
    month2 = "imix, ik, akbal, kan, chicchan, cimi, manik, lamat, muluk, ok, chuen, eb, ben, ix, mem, cib, caban, eznab, canac, ahau".split(", ")
    chk1["uayet"] = 18
    _a = int(a.strip("."))
    _c = int(c)
    sgm = 20 * (int(chk1[b])) + _a + _c * 365
    y = sgm // 260
    m = month2[(sgm+1) % 20 - 1]
    d = sgm % 13 + 1
    print(d, m, y)
