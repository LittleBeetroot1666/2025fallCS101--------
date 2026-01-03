matrix1 = []
matrix2 = []
for i in range(3):
    matrix1.append(input())
for i in range(3):
    matrix2.append(matrix1[-1 - i][::-1])

if matrix1 == matrix2:
    print('YES')
else:
    print('NO')
