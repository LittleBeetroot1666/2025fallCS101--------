def hanoi_3(n0):
    return 2 ** n0 - 1


def hanoi_4(n0):
    if n0 == 1:
        return 1
    elif n0 == 2:
        return 3
    else:
        listy_hanoi_4 = []
        for k0 in range(1, n0):
            jit_hanoi_4 = 2 * hanoi_4(n0 - k0) + hanoi_3(k0)
            listy_hanoi_4.append(jit_hanoi_4)
        return min(listy_hanoi_4)


for i in range(1, 13):
    print(hanoi_4(i))
