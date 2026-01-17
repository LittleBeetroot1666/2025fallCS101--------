wd = input()
up = 0
dn = 0
for char in wd:
    if 65 <= ord(char) <= 90:
        up += 1
    else:
        dn += 1
if up > dn:
    print(wd.upper())
else:
    print(wd.lower())
