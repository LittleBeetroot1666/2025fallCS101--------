n = int(input())
matrix = []
car = [_ for _ in range(n)]
loss = []
for c in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            loss.append(i)
        elif matrix[i][j] == 2:
            loss.append(j)
        elif matrix[i][j] == 3:
            loss.append(i)
            loss.append(j)
        else:
            null = 0

goodcar = []
cnt = 0
for i in range(n):
    if i in car and i not in loss:
        goodcar.append(i+1)
        cnt += 1

print(len(goodcar))
print(" ".join(map(str, goodcar)))
