for _ in range(int(input())):
    blacklist = 0
    x, y, z = map(int, input().split())
    xx = str(bin(x))[2:]
    lxx = len(xx)
    yy = str(bin(y))[2:]
    lyy = len(yy)
    zz = str(bin(z))[2:]
    lzz = len(zz)
    o = "0"
    clxx = 90 - lxx
    clyy = 90 - lyy
    clzz = 90 - lzz
    ltx = o * clxx + xx
    lty = o * clyy + yy
    ltz = o * clzz + zz

    for i in range(90):
        if (ltx[i] == "1" and lty[i] == "1" and ltz[i] == "0") or (ltx[i] == "1" and lty[i] == "0" and ltz[i] == "1") or (ltx[i] == "0" and lty[i] == "1" and ltz[i] == "1"):
            blacklist = 1
    if blacklist == 1:
        print("NO")
    else:
        print("YES")
