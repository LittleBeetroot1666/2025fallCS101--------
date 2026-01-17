k, n, w = list(map(int, input().split()))
t = 0
for i in range(1, w+1):
    t += i * k
if t <= n:
    print(0)
else:
    print(t-n)
