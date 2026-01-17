line = int(input())
for i in range(line):
    c0 = input()
    c = list(c0)
    t = []
    for cs in c:
        if cs.isdigit():
            t.append(int(cs))
        else:
            t.append(10)
    ds = t[0] * 7 + t[1] * 9 + t[2] * 10 + t[3] * 5 + t[4] * 8 + t[5] * 4 + t[6] * 2 + t[7] * 1 + t[8] * 6 + t[9] * 3 + t[10] * 7 + t[11] * 9 + t[12] * 10 + t[13] * 5 + t[14] * 8 + t[15] * 4 + t[16] * 2
    ktry = ds % 11
    if ktry+t[-1] == 1 or ktry+t[-1] == 12:
        print("YES")
    else:
        print("NO")
