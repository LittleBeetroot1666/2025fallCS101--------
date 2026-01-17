import sys

MOD = 10 ** 9 + 7

t, k = list(map(int, sys.stdin.readline().split()))

max_n = 10 ** 5
f = [0] * (max_n + 1)
f[0] = 1

for i in range(1, max_n + 1):
    f[i] = f[i - 1]
    if i >= k:
        f[i] += f[i - k]
    f[i] %= MOD

sum_ = [0] * (max_n + 1)
sum_[0] = f[0]
for i in range(1, max_n + 1):
    sum_[i] = (sum_[i - 1] + f[i]) % MOD

for _ in range(t):
    a, b = list(map(int, sys.stdin.readline().split()))
    res = (sum_[b] - sum_[a - 1]) % MOD
    print(res)
