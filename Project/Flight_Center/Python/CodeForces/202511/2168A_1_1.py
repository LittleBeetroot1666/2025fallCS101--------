# Welcome to visit my repo
# 0_toolcase
# auther: LittleBeetroot(The same name on CodeForces)

# ================ # k0j
def k0j(listy):
    return ''.join(listy)


# ================ # kpj
def kpj(listy):
    return ' '.join(listy)


# ================ # matrix_out_print
def matrix_out_print(amatrix):
    for arow in amatrix:
        print(kpj(arow))


# ================ # matrix_otto_print
def matrix_otto_print(amatrix):
    for arow in amatrix:
        print(k0j(arow))


# ================ # cartland
def cartland(n):
    if n == 0:
        c = 1
    else:
        c = 1
        for i in range(n):
            c = c * (4 * i + 2) // (i + 2)
    return c


# ================ # fry_chicken
def fry_chicken(listy, k):
    listy.sort(reverse=True)
    res0 = sum(listy) / k
    if listy[0] <= res0:
        return res0
    else:
        new_listy= listy[1:]
        nk = k-1
        return fry_chicken(new_listy, nk)


# ================ # mov_hanoi
def mov_hanoi(n0, a0, b0):
    return f'{n0}:{a0}->{b0}'


# ================ # solv_hanoi
def solv_hanoi(n0, a0, b0, c0):
    if n0 == 1:
        return [mov_hanoi(n0, a0, c0)]
    else:
        jit_sp_solv_hanoi = []
        for i in solv_hanoi(n0 - 1, a0, c0, b0):
            jit_sp_solv_hanoi.append(str(i))
        jit_sp_solv_hanoi.append(mov_hanoi(n0, a0, c0))
        for i in solv_hanoi(n0 - 1, b0, a0, c0):
            jit_sp_solv_hanoi.append(str(i))
        return jit_sp_solv_hanoi


# ================ # protect_matrix
def protect_matrix(amatrix):
    protected_matrix = [['#' for mati in range(len(amatrix[0]) + 2)]]
    for arow in amatrix:
        protected_row = ['#']
        for matj in range(len(amatrix[0])):
            protected_row.append(arow[matj])
        protected_row.append('#')
        protected_matrix.append(protected_row)
    protected_matrix.append(['#' for mati in range(len(amatrix[0]) + 2)])
    return protected_matrix


# ================ # protect_matrix0
def protect_matrix0(amatrix):
    protected_matrix = [['0' for mati in range(len(amatrix[0]) + 2)]]
    for arow in amatrix:
        protected_row = ['0']
        for matj in range(len(amatrix[0])):
            protected_row.append(arow[matj])
        protected_row.append('0')
        protected_matrix.append(protected_row)
    protected_matrix.append(['0' for mati in range(len(amatrix[0]) + 2)])
    return protected_matrix


# ================ # protect_matrix_awith
def protect_matrix_awith(amatrix, withto_a):
    protected_matrix = [[withto_a for mati in range(len(amatrix[0]) + 2)]]
    for arow in amatrix:
        protected_row = [withto_a]
        for matj in range(len(amatrix[0])):
            protected_row.append(arow[matj])
        protected_row.append(withto_a)
        protected_matrix.append(protected_row)
    protected_matrix.append([withto_a for mati in range(len(amatrix[0]) + 2)])
    return protected_matrix


# ================ # mount
def mount(listie):
    mount_altitude = [0]
    for i in range(1, len(listie)):
        if listie[i] > listie[i - 1]:
            mount_altitude.append(mount_altitude[-1] + 1)
        elif listie[i] < listie[i - 1]:
            mount_altitude.append(mount_altitude[-1] - 1)
        else:
            mount_altitude.append(mount_altitude[-1])
    base_altitude = min(mount_altitude) - 1
    mount_waterfill = -len(listie) * base_altitude
    mount_seasum = sum(mount_altitude)
    mount_landsum = mount_seasum + mount_waterfill
    return mount_landsum


# ================ # up
def up(sest_001):
    blacklist_001 = 0
    if len(sest_001) == 1:
        return True
    else:
        for _ in range(len(sest_001) - 1):
            if sest_001[_] > sest_001[_ + 1]:
                blacklist_001 += 1
        if blacklist_001 == 0:
            return True
        else:
            return False


# ================ # poup
def poup(sest_002):
    while not up(sest_002):
        for _ in range(len(sest_002) - 1):
            if sest_002[_] > sest_002[_ + 1]:
                sest_002[_], sest_002[_ + 1] = sest_002[_ + 1], sest_002[_]
    return sest_002


# ================ # 2_sqr
def _2sqr(x0, y0, x1, y1):
    if abs(x0 - x1) == abs(y0 - y1):
        return True
    else:
        return False


L_toj = input()
if L_toj == 'first':
    n = int(input())
    nums = list(map(int, input().split()))
    js = []
    for num in nums:
        if num == 1:
            js.append('a')
        elif num == 2:
            js.append('b')
        elif num == 3:
            js.append('c')
        elif num == 4:
            js.append('d')
        elif num == 5:
            js.append('e')
        elif num == 6:
            js.append('f')
        elif num == 7:
            js.append('g')
        elif num == 8:
            js.append('h')
        elif num == 9:
            js.append('i')
        elif num == 10:
            js.append('j')
        elif num == 11:
            js.append('k')
        elif num == 12:
            js.append('l')
        elif num == 13:
            js.append('m')
        elif num == 14:
            js.append('n')
        elif num == 15:
            js.append('o')
        elif num == 16:
            js.append('p')
        elif num == 17:
            js.append('q')
        elif num == 18:
            js.append('r')
        elif num == 19:
            js.append('s')
        elif num == 20:
            js.append('t')
        elif num == 21:
            js.append('u')
        elif num == 22:
            js.append('v')
        elif num == 23:
            js.append('w')
        elif num == 24:
            js.append('x')
        elif num == 25:
            js.append('y')
        elif num == 26:
            js.append('z')

    print(k0j(js))

else:
    js = input()
    nums = []
    for j in js:
        if j == 'a':
            nums.append('1')
        elif j == 'b':
            nums.append('2')
        elif j == 'c':
            nums.append('3')
        elif j == 'd':
            nums.append('4')
        elif j == 'e':
            nums.append('5')
        elif j == 'f':
            nums.append('6')
        elif j == 'g':
            nums.append('7')
        elif j == 'h':
            nums.append('8')
        elif j == 'i':
            nums.append('9')
        elif j == 'j':
            nums.append('10')
        elif j == 'k':
            nums.append('11')
        elif j == 'l':
            nums.append('12')
        elif j == 'm':
            nums.append('13')
        elif j == 'n':
            nums.append('14')
        elif j == 'o':
            nums.append('15')
        elif j == 'p':
            nums.append('16')
        elif j == 'q':
            nums.append('17')
        elif j == 'r':
            nums.append('18')
        elif j == 's':
            nums.append('19')
        elif j == 't':
            nums.append('20')
        elif j == 'u':
            nums.append('21')
        elif j == 'v':
            nums.append('22')
        elif j == 'w':
            nums.append('23')
        elif j == 'x':
            nums.append('24')
        elif j == 'y':
            nums.append('25')
        elif j == 'z':
            nums.append('26')

    print(len(js))
    print(kpj(nums))
