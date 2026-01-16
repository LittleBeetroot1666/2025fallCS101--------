n = int(input())
js = list(map(int, input().split()))
js1 = []
sq = []
for i in range(n):
    sq.append([js[i],i])
sq.sort()

for i in range(n):
    js1.append(sq[i][1]+1)
print(" ".join(map(str,js1)))

sgm = 0
su = 0
js.sort()
for i in range(n):
    sgm += su
    su += js[i]
k_out = sgm / n
print("%.2f" % k_out)
