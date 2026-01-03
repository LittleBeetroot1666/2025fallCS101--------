def tpp(a0, b0):
    if a0 % b0 == 0:
        return a0
    else:
        return (a0 % b0) * (a0 // b0 + 1)


n, m, s = list(map(int, input().split()))
print(tpp(m, s) * tpp(n, s))
