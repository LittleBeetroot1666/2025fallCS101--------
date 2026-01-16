def kpj(listy):
    return ' '.join(listy)


Lne = int(input())
for _ in range(Lne):
    n = int(input())
    visited = [[False] * n for _ in range(n)]
    matrix = []
    for i in range(n):
        row = []
        row_root = input()
        for rr0 in row_root:
            row.append(rr0)
        matrix.append(row)
    red = 0
    black = 0

    def dfs_pm(i0, j0, tara):
        if i0 < 0 or i0 >= n or j0 < 0 or j0 >= n:
            return
        if visited[i0][j0]:
            return
        if matrix[i0][j0] != tara:
            return
        visited[i0][j0] = True
        dfs_pm(i0 + 1, j0, tara)
        dfs_pm(i0 - 1, j0, tara)
        dfs_pm(i0, j0 + 1, tara)
        dfs_pm(i0, j0 - 1, tara)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'r' and not visited[i][j]:
                red += 1
                dfs_pm(i, j, 'r')
            elif matrix[i][j] == 'b' and not visited[i][j]:
                black += 1
                dfs_pm(i, j, 'b')

    print(red, black)
