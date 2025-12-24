def protect_matrix0(amatrix):
    protected_matrix = [['0' for mati in range(len(amatrix[0]) + 2)]]
    for arow in amatrix:
        protected_row = ['0']
        for matj in range(len(amatrix[0])):
            protected_row.append(arow[matj])
        protected_row.append('0')
        protected_matrix.append(protected_row)
    protected_matrix.append(['0' for mati in range(len(amatrix[0]) + 2)])
    return protected_matrix
