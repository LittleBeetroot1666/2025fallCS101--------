n = int(input())
p = 0
s = 0
for t in list(map(int, input().split())):
    p += t
    if t < 0 and p < 0:
        s += 1
        p = 0
print(s)
