line = int(input())
for i in range(line):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sgm_1 = sgm_2 = 0
    for j in range(n):
        sgm_1 += a[j]
        sgm_2 += b[j]
    sgm_1 += n * min(b)
    sgm_2 += n * min(a)
    if sgm_1 > sgm_2:
        print(sgm_2)
    else:
        print(sgm_1)
