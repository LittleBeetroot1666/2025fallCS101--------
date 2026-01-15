l = int(input())
n = int(input())
js = list(map(int, input().split()))
ks = []
for j in js:
    if j <= l // 2:
        ks.append(j)
    else:
        ks.append(l + 1 - j)
print(max(ks), l + 1 - min(ks))
