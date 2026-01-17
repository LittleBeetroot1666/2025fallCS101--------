n = int(input())
js = list(map(int, input().split()))
sgm = 0
earn = 0
for i in js:
    sgm += i
greed = (sgm+2) // 2
trick = sorted(js, reverse=True)
j = 0
while earn < greed:
    earn += int(trick[j])
    j += 1
print(j)
