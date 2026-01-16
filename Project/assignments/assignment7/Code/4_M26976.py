n = int(input())
js = list(map(int, input().split()))

if n == 1 or max(js) - min(js) == 0:
    print(1)
elif n == 2 and js[0]!=js[1]:
    print(2)
else:
    k = 0

    stt = 1
    v = 0
    ks = [js[i] - js[i - 1] for i in range(1, n)]
    if 0 in ks:
        ks.remove(0)
    if ks[0] < 0:
        stt = -1

    for i in range(0, len(ks)):
        if ks[i] // stt > 0:
            stt *= (-1)
            k += 1

    print(k + 1)
