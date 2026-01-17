a, b = list(map(int, input().split()))
s = 0
ts = []
for t in range(a, b+1):
    i = t//100
    j = t % 100 // 10
    k = t % 10
    if i ** 3 + j ** 3 + k ** 3 == t:
        ts.append(t)
if len(ts) == 0:
    print("NO")
else:
    print(*ts, sep=" ")
