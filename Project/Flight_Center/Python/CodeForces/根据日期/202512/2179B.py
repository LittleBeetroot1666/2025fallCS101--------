for _ in range(int(input())):
    n = int(input())
    js = list(map(int, input().split()))
    ps = []
    rs = [abs(js[1] - js[0]), abs(js[-2] - js[-1])]
    for j in range(n - 1):
        ps.append(abs(js[j + 1] - js[j]))
    for k in range(n - 2):
        if (js[k] > js[k + 1] and js[k + 1] < js[k + 2]) or (js[k] < js[k + 1] and js[k + 1] > js[k + 2]):
            rs.append(2 * min(ps[k], ps[k + 1]))
    print(sum(ps) - max(rs))
