import sys


def solve():
    n, m = map(int, sys.stdin.readline().split())
    nums = []
    s = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        nums.append(x)
        s.append(x + y)
    min_sum = min(s)
    ans = 0
    nums.sort()
    pre = [0]
    for ni in nums:
        pre.append(pre[-1] + ni)
    for i, p in enumerate(pre):
        ans = max(ans, ((m - p) // min_sum) * 2 + i)
    print(ans)


if __name__ == "__main__":
    solve()
