n = int(input())
js0 = list(map(int, input().split()))
js = [0]
for i in range(len(js0)):
    js.append(js0[i])
js.append(0)
s = int(input())
for ss in range(s):
    i, t = map(int, input().split())
    js[i - 1] += t - 1
    js[i + 1] += js[i] - t
    js[i] = 0
for i in range(1, len(js) - 1):
    print(js[i])
