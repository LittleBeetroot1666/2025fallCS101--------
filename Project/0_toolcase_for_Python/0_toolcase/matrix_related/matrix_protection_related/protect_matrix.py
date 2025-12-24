def protect_matrix(amatrix):
    protected_matrix = [['#' for mati in range(len(amatrix[0]) + 2)]]
    for arow in amatrix:
        protected_row = ['#']
        for matj in range(len(amatrix[0])):
            protected_row.append(arow[matj])
        protected_row.append('#')
        protected_matrix.append(protected_row)
    protected_matrix.append(['#' for mati in range(len(amatrix[0]) + 2)])
    return protected_matrix
