ts = [n * (n + 1) // 2 for n in range(1, 200)]
t = int(input())
if t in ts:
    print('YES')
else:
    print('NO')
