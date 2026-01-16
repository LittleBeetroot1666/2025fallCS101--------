MOD = 10**9 + 7
max_n = 10**6
fact = [1] * (max_n + 1)
inv = [1] * (max_n + 1)

for i in range(1, max_n + 1):
    fact[i] = fact[i-1] * i % MOD

inv[max_n] = pow(fact[max_n], MOD-2, MOD)
for i in range(max_n-1, -1, -1):
    inv[i] = inv[i+1] * (i+1) % MOD


def combination(n0, k0):
    if k0 < 0 or k0 > n0:
        return 0
    return fact[n0] * inv[k0] % MOD * inv[n0 - k0] % MOD


t, k = list(map(int, input().split()))
for _ in range(t):
    a, b = list(map(int, input().split()))
    sgm = 0
    ts = []
    for i in range(1, 10**5 + 1):
        tt = 0
        sgm0 = 0
        while i >= tt:
            sgm0 += combination(i, tt)
            i -= (k - 1)
            tt += 1
        ts.append(sgm0)
    for n in range(a, b + 1):
        sgm += ts[n]
    print(sgm % MOD)
