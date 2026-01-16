import sys

dir8 = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
cnt = 0


def dfs(x, y, tara):
    global cnt
    if matrix[x][y] == tara:
        matrix[x][y] = '.'
        cnt += 1
        for dirr in dir8:
            dfs(x + dirr[0], y + dirr[1], tara)
    else:
        cnt += 0


for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    ress = [0]

    matrix = [['.' for _ in range(m + 2)] for _ in range(n + 2)]
    for row in range(1, n + 1):
        matrix[row][1: -1] = sys.stdin.readline()

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i][j] == 'W':
                cnt = 0
                dfs(i, j, 'W')
                ress.append(cnt)

    print(max(ress))
