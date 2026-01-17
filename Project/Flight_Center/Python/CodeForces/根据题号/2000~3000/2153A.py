l = int(input())
for i in range(l):
    n = int(input())
    ps = list(map(int, input().split()))
    js = []
    for p in ps:
        if p not in js:
            js.append(p)
    print(len(js))
