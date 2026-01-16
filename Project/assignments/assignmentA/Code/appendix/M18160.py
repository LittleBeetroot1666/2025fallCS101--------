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


def countig_block(amatrix, i0, j0, tara):
    cnt = 0
    dir0 = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    if amatrix[i0][j0] == tara:
        amatrix[i0][j0] = '.'
        cnt += 1
    for d0 in dir0:
        cnt += countig_block(amatrix, i0 + d0[0], j0 + d0[1], tara)
    return cnt


Lne = int(input())
for _ in range(Lne):
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
                res.append(countig_block(pamatrix, i, j, 'W'))

    print(max(res))
