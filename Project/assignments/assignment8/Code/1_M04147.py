def mov_hanoi(n0, a0, b0):
    return f'{n0}:{a0}->{b0}'


def solv_hanoi(n0, a0, b0, c0):
    if n0 == 1:
        return [mov_hanoi(n0, a0, c0)]
    else:
        jit_sp_solv_hanoi = []
        for i in solv_hanoi(n0 - 1, a0, c0, b0):
            jit_sp_solv_hanoi.append(str(i))
        jit_sp_solv_hanoi.append(mov_hanoi(n0, a0, c0))
        for i in solv_hanoi(n0 - 1, b0, a0, c0):
            jit_sp_solv_hanoi.append(str(i) )
        return jit_sp_solv_hanoi


n, a, b, c = list(map(str,input().split()))
n_int = int(n)
js = solv_hanoi(n_int, a, b, c)
for j in js:
    print(j)
