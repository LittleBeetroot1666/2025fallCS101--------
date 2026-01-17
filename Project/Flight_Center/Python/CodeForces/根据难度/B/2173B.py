for _ in range(int(input())):
    n = int(input())
    amat = [0, 0]
    rs = list(map(int, input().split()))
    bs = list(map(int, input().split()))
    for i in range(n):
        amat = [max(amat[0] - rs[i], bs[i] - amat[1]), min(amat[1] - rs[i], bs[i] - amat[0])]

    print(amat[0])
