n, m = list(map(int, input().split()))
matrix = []
row0 = [0 for i in range(m + 2)]
matrix.append(row0)
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    row1 = [0]
    for j in range(m):
        row1.append(row[j])
    row1.append(0)
    matrix.append(row1)
matrix.append(row0)

new_matrix = []
for i in range(1, n + 1):
    new_row = []
    for j in range(1, m + 1):
        new_row.append(matrix[i][j])
    new_matrix.append(new_row)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sgm = matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][j + 1] + matrix[i][j - 1] + matrix[i][j + 1] + matrix[i + 1][j - 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if matrix[i][j] == 1:
            if 2 <= sgm <= 3:
                new_matrix[i - 1][j - 1] = 1
            else:
                new_matrix[i - 1][j - 1] = 0
        if matrix[i][j] == 0:
            if sgm == 3:
                new_matrix[i - 1][j - 1] = 1
            else:
                new_matrix[i - 1][j - 1] = 0



for new_row in new_matrix:
    print(*new_row)
