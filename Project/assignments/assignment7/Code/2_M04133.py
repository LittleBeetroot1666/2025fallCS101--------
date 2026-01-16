d = int(input())
n = int(input())
matrix = [[0 for i in range(1025)] for j in range(2025)]
js = []
for _ in range(n):
    x, y, h = list(map(int, input().split()))
    for i in range(max(x - d, 0), min(x + d + 1, 1025)):
        for j in range(max(y - d, 0), min(y + d + 1, 1025)):
            matrix[i][j] += h
for i in range(1025):
    for j in range(1025):
        js.append(matrix[i][j])
js.sort(reverse=True)
cnt = 0
while js[cnt] == js[0]:
    cnt += 1
print(cnt, js[0])
