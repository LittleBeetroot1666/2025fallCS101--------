n = int(input())
js = list(map(int, input().split()))
s = []
s1 = 0
s2 = 0
s3 = 0
s4 = 0
t = 0
for j in js:
    s.append(j)
for i in s:
    if i == 4:
        s4 += 1
    elif i == 3:
        s3 += 1
    elif i == 2:
        s2 += 1
    else:
        s1 += 1
t += s4
t += s3
s1 -= s3
if s2 % 2 == 0:
    t += s2 // 2
else:
    t += s2 // 2
    t += 1
    s1 -= 2
if s1 <= 0:
    t += 0
else:
    t += (s1 + 3) // 4
print(t)
