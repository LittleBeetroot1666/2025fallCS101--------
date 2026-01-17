ipt = input()
r = []
for i in range(1, 4000):
    ip = i
    null = 0
    if ip < 4000:
        i = int(ip)
        Rom = []
        t = i // 1000
        h = i % 1000 // 100
        m = i % 100 // 10
        s = i % 10
        if t == 3:
            Rom.append("MMM")
        elif t == 2:
            Rom.append("MM")
        elif t == 1:
            Rom.append("M")
        else:
            null = 0
        if h == 9:
            Rom.append("CM")
        elif h == 8:
            Rom.append("DCCC")
        elif h == 7:
            Rom.append("DCC")
        elif h == 6:
            Rom.append("DC")
        elif h == 5:
            Rom.append("D")
        elif h == 4:
            Rom.append("CD")
        elif h == 3:
            Rom.append("CCC")
        elif h == 2:
            Rom.append("CC")
        elif h == 1:
            Rom.append("C")
        else:
            null = 0
        if m == 9:
            Rom.append("XC")
        elif m == 8:
            Rom.append("LXXX")
        elif m == 7:
            Rom.append("LXX")
        elif m == 6:
            Rom.append("LX")
        elif m == 5:
            Rom.append("L")
        elif m == 4:
            Rom.append("XL")
        elif m == 3:
            Rom.append("XXX")
        elif m == 2:
            Rom.append("XX")
        elif m == 1:
            Rom.append("X")
        else:
            null = 0
        if s == 9:
            Rom.append("IX")
        elif s == 8:
            Rom.append("VIII")
        elif s == 7:
            Rom.append("VII")
        elif s == 6:
            Rom.append("VI")
        elif s == 5:
            Rom.append("V")
        elif s == 4:
            Rom.append("IV")
        elif s == 3:
            Rom.append("III")
        elif s == 2:
            Rom.append("II")
        elif s == 1:
            Rom.append("I")
        else:
            null = 0
        rom = "".join(map(str, Rom))
        r.append(rom)
    else:
        null = 0
if ipt.isdigit():
    d = int(ipt)-1
    print(r[d])
else:
    j = 0
    while r[j] != ipt:
        j = j + 1
    print(j + 1)
