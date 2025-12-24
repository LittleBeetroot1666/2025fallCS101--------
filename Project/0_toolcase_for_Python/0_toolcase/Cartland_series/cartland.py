def cartland(n):
    if n == 0:
        c = 1
    else:
        c = 1
        for i in range(n):
            c = c * (4 * i + 2) // (i + 2)
    return c
