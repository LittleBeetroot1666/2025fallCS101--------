k = int(input())
js = list(map(int, input().split()))
ts = [[j, 1] for j in js]
for i in range(1, k + 1):
    spl = [0]
    for t in range(k - i + 1, k):
        if ts[t][0] <= ts[k - i][0]:
            spl.append(ts[t][1])
        ts[k - i][1] = max(spl) + 1

res = [t[1] for t in ts]
print(max(res))
