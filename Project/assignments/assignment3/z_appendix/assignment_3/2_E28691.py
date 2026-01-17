ipt = input().strip()
js = []
for i in ipt:
    if i.isdigit():
        js.append(int(i))
sgm = 10 * js[0] + js[1] + 10 * js[2] + js[3]
print(sgm)
