k = int(input())
ki = k % 26
L = []
nums = []
Lplus = []
st = input()
string = list(st)
for s in string:
    L.append(s)
for i in L:
    if 64 <= ord(i) <= 90:
        t = ord(i)-ki
        if t <= 64:
            t += 26
        ts = chr(t)
        Lplus.append(ts)
    elif 97 <= ord(i) <= 123:
        t = ord(i) - ki
        if t < 97:
            t += 26
        ts = chr(t)
        Lplus.append(ts)
result = "".join(Lplus)
print(result)
