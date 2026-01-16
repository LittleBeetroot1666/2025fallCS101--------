def div(n0, k0):
    if k0 == 1:
        return 1
    elif k0 == 2:
        return n0 // 2
    else:
        res = 0
        i = 0
        while n0 - i * k0 - 1 >= 2:
            res += div(n0 - i * k0 - 1, k0 - 1)
            i += 1
        return res


def solve():
    n = int(input())
    sgm = 0
    for i in range(1, n + 1):
        sgm += div(n, i)
    print(sgm)


while True:
    try:
        if __name__ == '__main__':
            solve()
    except:
        break
