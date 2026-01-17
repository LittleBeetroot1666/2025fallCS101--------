n = int(input())
js = list(map(int, input().split()))
sgm = 0
s = []
for j in js:
    sgm += j
    s.append(sgm)
m = min(s)
if m < 0:
    res = 1 - m
else:
    res = 1
print(res)
