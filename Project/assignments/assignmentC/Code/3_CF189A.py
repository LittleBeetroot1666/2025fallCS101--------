from functools import lru_cache
import sys
sys.setrecursionlimit(180000)


n0, a0, b0, c0 = list(map(int, input().split()))


@lru_cache(maxsize=None)
def dp(n, a, b, c):
    if n < 0:
        return -10000
    elif n == 0:
        return 0
    else:
        return max(dp(n - a, a, b, c) + 1, dp(n - b, a, b, c) + 1, dp(n - c, a, b, c) + 1)


if n0 % min(a0, b0, c0) == 0:
    print(n0 // min(a0, b0, c0))
else:
    print(dp(n0, a0, b0, c0))
