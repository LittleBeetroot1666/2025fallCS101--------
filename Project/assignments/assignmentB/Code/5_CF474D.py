MOD = 10 ** 9 + 7

t, k = list(map(int, input().split()))

f = [0] * (10 ** 5 + 1)
f[0] = 1

for i in range(1, 10 ** 5 + 1):
    f[i] = f[i - 1]
    if i >= k:
        f[i] += f[i - k]
        # 当i>=k时，即f[i] = f[i - 1] + f[i - k]
    f[i] %= MOD

sgm = [0] * (10 ** 5 + 1)
sgm[0] = f[0]
for i in range(1, 10 ** 5 + 1):
    sgm[i] = (sgm[i - 1] + f[i]) % MOD

for _ in range(t):
    a, b = list(map(int, input().split()))
    res = (sgm[b] - sgm[a - 1]) % MOD
    print(res)
