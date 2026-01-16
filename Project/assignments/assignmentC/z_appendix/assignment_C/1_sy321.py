import sys

dir4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve():
    n, m = list(map(int, sys.stdin.readline().split()))
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    fa = {}

    def bfs(i, j):
        if matrix[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            for di, dj in dir4:
                if 0 <= i + di <= n - 1 and 0 <= j + dj <= m - 1:
                    if matrix[i + di][j + dj] == 0 and not visited[i + di][j + dj]:
                        fa[(i + di, j + dj)] = (i, j)
                    bfs(i + di, j + dj)

    bfs(0, 0)

    res = [(n - 1, m - 1)]
    while (0, 0) not in res:
        res.append(fa[res[-1]])
    ress = res[::-1]
    for r in ress:
        print(r[0] + 1, r[1] + 1)


if __name__ == '__main__':
    solve()
