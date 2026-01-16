def kcj(listy):
    return ','.join(listy)


m, n, k = map(int, input().split(','))
mkf = [[]for _ in range(9999)]
for i in range(m + 1, n):
    ts = i // 1000 + i % 1000 // 100 + i % 100 // 10 + i % 10
    if ts % k == 0:
        mkf[ts // k].append(str(i))

for row in mkf:
    if len(row) > 0:
        print(kcj(row))
