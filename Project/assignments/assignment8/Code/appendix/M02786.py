def pell(n0pell):
    if n0pell == 0:
        return 0
    elif n0pell == 1:
        return 1
    elif n0pell == 2:
        return 2
    else:
        return 2 * pell(n0pell - 1) + pell(n0pell - 2)


Lne = int(input())
for _L in range(Lne):
    i = int(input())
    print(pell(i) % 32767)
