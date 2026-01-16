n, b = list(map(int, input().split()))
prices = list(map(int, input().split()))
weights = list(map(int, input().split()))
js = []
for i in range(n):
    js.append([prices[i], weights[i], False])
earns = [0]


def dfs(js0, b0):
    earn = 0
    if b0 >= js0[0][1]:
        js0[0][2] = True
        if len(js0) >= 2:
            dfs(js0[1:], b0 - js0[0][1])
        for j in js:
            if j[2] is True:
                earn += j[0]
        earns.append(earn)
        earn -= earn

    js0[0][2] = False
    if len(js0) >= 2:
        dfs(js0[1:], b0)


dfs(js, b)
print(max(earns))
