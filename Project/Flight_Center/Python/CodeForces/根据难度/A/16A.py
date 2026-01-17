n, m = list(map(int, input().split()))
forbidden = -1
target_div = int('1' * m)
valid = True
for _ in range(n):
    nl = int(input())
    if nl % target_div != 0:
        valid = False
        break
    hav_tag = nl // target_div
    if hav_tag == forbidden:
        valid = False
        break
    else:
        forbidden = hav_tag

if valid:
    print('YES')
else:
    print('NO')
