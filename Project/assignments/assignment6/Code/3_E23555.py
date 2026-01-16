n, m1, m2 = map(int, input().split())
A = [[0 for x1 in range(n)] for y1 in range(n)]
B = [[0 for x2 in range(n)] for y2 in range(n)]
C = [[0 for x3 in range(n)] for y3 in range(n)]
for i in range(m1):
    a, b, k = map(int, input().split())
    A[a][b] = k
for i in range(m2):
    a, b, k = map(int, input().split())
    B[a][b] = k
for i1 in range(n):
    for j1 in range(n):
        res = 0
        for t in range(n):
            res += A[i1][t] * B[t][j1]
        C[i1][j1] = res

for a1 in range(n):
    for b1 in range(n):
        if C[a1][b1] != 0:
            print(a1, b1, C[a1][b1])
