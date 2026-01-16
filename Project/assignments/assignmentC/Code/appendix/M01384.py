from functools import lru_cache
import sys
sys.setrecursionlimit(180000)


@lru_cache(maxsize=None)
def dp(n, mat0):
    if n < 0:
        return float('inf')
    elif n == 0:
        return 0
    else:
        return min(dp(n - t[2], mat0) + t[1] for t in mat0)


for _ in range(int(sys.stdin.readline())):
    e, f = list(map(int, sys.stdin.readline().split()))
    piget = f - e
    matt = []
    for _ in range(int(sys.stdin.readline())):
        p, w = list(map(int, sys.stdin.readline().split()))
        matt.append([p / w, p, w])
    matt.sort()
    mat = tuple(tuple(item) for item in matt)

    res = dp(piget, mat)
    if res == float('inf'):
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {res}.')
