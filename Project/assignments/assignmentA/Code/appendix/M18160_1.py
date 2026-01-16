def protect_matrix_awith(amatrix, withto_a):
    protected_matrix = [[withto_a for mati in range(len(amatrix[0]) + 2)]]
    for arow in amatrix:
        protected_row = [withto_a]
        for matj in range(len(amatrix[0])):
            protected_row.append(arow[matj])
        protected_row.append(withto_a)
        protected_matrix.append(protected_row)
    protected_matrix.append([withto_a for mati in range(len(amatrix[0]) + 2)])
    return protected_matrix


cnt0 = 0


def getig_block(amatrix, i0, j0, tara):
    dir0 = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    if amatrix[i0][j0] == tara:
        amatrix[i0][j0] = '.'
        global cnt0
        cnt0 += 1
    for d0 in dir0:
        getig_block(amatrix, i0 + d0[0], j0 + d0[1], tara)


def countig_block(amatrix, i0, j0, tara):
    getig_block(amatrix, i0, j0, tara)
    return cnt0


Lne = int(input())
for _ in range(Lne):
    cnt0 = 0
    res = []
    n, m = list(map(int, input().split()))
    matrix = []
    for rrow in range(n):
        row0 = input()
        row = []
        for ri in row0:
            row.append(ri)
        matrix.append(row)
    pamatrix = protect_matrix_awith(matrix, '.')
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pamatrix[i][j] == 'W':
                countig_block(pamatrix, i, j, 'W')
                res.append(cnt0)
                cnt0 = 0

    print(max(res))
