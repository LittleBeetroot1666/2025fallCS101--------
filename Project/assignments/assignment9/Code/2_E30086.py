n, d = list(map(int, input().split()))
js = list(map(int, input().split()))
js.sort()
blacklist = 0
for i in range(n):
    if js[2 * i + 1] - js[2 * i] > d:
        blacklist += 1
if blacklist > 0:
    print('No')
else:
    print('Yes')
