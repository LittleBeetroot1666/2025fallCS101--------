l = int(input())
for _ in range(l):
    n, m = list(map(int, input().split()))
    if n >= 2:
        js = [i for i in range(m)]
        crispr = []
        for _ in range(2):
            for i0 in js:
                crispr.append(i0)
        origin_matrix = []
        for j in range(1, m):
            row = [str(crispr[c]) for c in range(j, m + j)]
            origin_matrix.append(row)
        if m == 1:
            haj = 0
            for tt in range(n + 1):
                print(0)
                null = 0
        else:
            if n >= m - 1:
                haj = m
            else:
                haj = n + 1
            print(haj)

            for p in range(1, n + 1):
                tg = p % m - 1
                print(' '.join(origin_matrix[tg][ts] for ts in range(m)))
    else:
        if m == 1:
            haj = 0
            for tt in range(n + 1):
                print(0)
                null = 0
        else:
            print(2)
            tw = [str(j) for j in range(m)]
            print(' '.join(tw))
