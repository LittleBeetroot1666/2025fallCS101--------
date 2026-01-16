dir4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cnt = 0


def visitable(i, j):
    if 0 <= i <= n - 1 and 0 <= j <= m - 1 and matrix[i][j] == 1:
        return True
    else:
        return False


n, m = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]


def dfs(i, j):
    if visitable(i, j) and not visited[i][j]:
        visited[i][j] = True
        for di, dj in dir4:
            dfs(i + di, j + dj)


for i0 in range(n):
    for j0 in range(m):
        if matrix[i0][j0] == 1 and not visited[i0][j0]:
            cnt += 1
            dfs(i0, j0)

print(cnt)
