def permute0(listy):
    if len(listy) == 1:
        return [[listy[0]]]
    else:
        al_listy = []
        for j_in_listy in listy:
            n_listy = [j_in_listy]
            listy0 = listy[:]
            listy0.remove(j_in_listy)
            for k_in_listyf in permute0(listy0):
                for k_in_listy in k_in_listyf:
                    n_listy.append(k_in_listy)
                al_listy.append(n_listy)
                n_listy = [j_in_listy]
        return al_listy


n = int(input())
res = float('inf')
matrix = [list(map(int, input().split())) for _ in range(n)]
alm = permute0([i for i in range(1, n)])
for a0 in alm[:len(alm)//2]:
    res0 = 0
    for i in range(len(a0) - 1):
        res0 += matrix[a0[i]][a0[i + 1]]
    res0 += matrix[0][a0[0]]
    res0 += matrix[a0[n - 2]][0]
    res = min(res, res0)

print(res)
