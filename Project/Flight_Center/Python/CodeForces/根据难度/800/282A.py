s = 0
l = int(input())
for i in range(l):
    st = str(input())
    if st[0] == '+' or st[1] == '+':
        s += 1
    elif st[0] == '-' or st[1] == '-':
        s -= 1
print(s)
