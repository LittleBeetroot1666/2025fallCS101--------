n, m = map(int, input().split())
js = []
sgm = 0
earn = 0
for _ in range(n):
    v,w = map(int, input().split())
    js.append((v / w,v,w))
js.sort(reverse=True)
for j in js:
    if sgm + j[2] <= m:
        sgm += j[2]
        earn += j[1]
    else:
        earn += j[0] * (m - sgm)
        sgm = m
        break
print("%.2f" % earn)
