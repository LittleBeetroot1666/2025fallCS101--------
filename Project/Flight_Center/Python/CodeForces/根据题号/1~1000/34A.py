n = int(input())
js = list(map(int, input().split()))
pre_res = [[n, 1]]
mmi = abs(js[-1] - js[0])
for i in range(len(js) - 1):
    if abs(js[i] - js[i + 1]) <= mmi:
        mmi = abs(js[i] - js[i + 1])
        pre_res.append([i + 1, i + 2])
print(pre_res[-1][0], pre_res[-1][1])
