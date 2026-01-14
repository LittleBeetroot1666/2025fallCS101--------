n, m = list(map(int, input().split()))
matrix = [input() for _ in range(n)]
rnt_i = 0
rnt_j = n - 1
int_i = 0
blacklist_i = 0
int_j = m - 1
blacklist_j = 0
while matrix[rnt_i] == '.' * m:
    rnt_i += 1
while matrix[rnt_j] == '.' * m:
    rnt_j -= 1
while blacklist_i == 0:
    for j in range(n):
        if matrix[j][int_i] == '*':
            blacklist_i += 1
            break
    if blacklist_i == 0:
        int_i += 1
while blacklist_j == 0:
    for j in range(n):
        if matrix[j][int_j] == '*':
            blacklist_j += 1
            break
    if blacklist_j == 0:
        int_j -= 1

for _ in range(rnt_i, rnt_j + 1):
    print(matrix[_][int_i: int_j + 1])
