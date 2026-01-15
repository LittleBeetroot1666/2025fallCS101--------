n = int(input())
res = float('inf')
matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[float('inf')] * n for _ in range(1 << n)]
dp[1 << 0][0] = 0

for mask in range(1 << n):
    for u in range(n):
        if not (mask & (1 << u)):
            continue
        for v in range(n):
            if mask & (1 << v):
                continue
            new_mask = mask | (1 << v)

            if dp[new_mask][v] > dp[mask][u] + matrix[u][v]:
                dp[new_mask][v] = dp[mask][u] + matrix[u][v]

full_mask = (1 << n) - 1
for u in range(n):
    res = min(res, dp[full_mask][u] + matrix[u][0])

print(res)
