lines = int(input())
for i in range(lines):
    n = int(input())
    js = list(map(int, input().split()))
    jt = []
    for j in js:
        if j not in jt:
            jt.append(j)
    p = len(jt)
    print(2 * p - 1)
