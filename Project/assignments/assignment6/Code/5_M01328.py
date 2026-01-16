n, m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

C = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            C += 4

for i in range(n):
    for j in range(m-1):
        if matrix[i][j] + matrix[i][j+1] == 2:
            C -= 2

for j in range(m):
    for i in range(n-1):
        if matrix[i][j] + matrix[i+1][j] == 2:
            C -= 2

print(C)
