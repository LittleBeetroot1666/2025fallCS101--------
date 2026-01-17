n = int(input())
p = 0
s = 0
ts = list(map(int, input().split()))
for t in ts:
    p += t
    if t < 0 and p < 0:
        s += 1
        p = 0
print(s)
