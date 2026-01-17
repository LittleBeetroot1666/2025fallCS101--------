n, lne = list(map(int, input().split()))
js = []
sgm = 0
for ijs in range(1, n+2):
    js.append(1)
for il in range(1, lne+1):
    a, b = list(map(int, input().split()))
    for t in range(a, b+1):
        js[t] = 0
for i in js:
    sgm += i
print(sgm)
