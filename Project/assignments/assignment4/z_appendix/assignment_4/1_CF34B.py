n,m = map(int,input().split())
tvs = list(map(int,input().split()))
wage = 0
pre_target = []
for i in tvs:
    if i < 0:
        pre_target.append(-i)
target = sorted(pre_target, reverse=True)
p = 0
while p < m and p < len(target):
    wage += int(target[p])
    p += 1
print(wage)
