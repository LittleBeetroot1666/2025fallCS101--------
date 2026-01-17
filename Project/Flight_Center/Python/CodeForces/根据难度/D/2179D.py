import re

js = [[] for _ in range(17)]
ps = [str(2 * _) for _ in range(2 ** 15)]
for i in range(2 ** 16):
    for j in range(16, 0, -1):
        if i % (2 ** j) == 2 ** j - 1:
            js[16 - j].append(str(i))
            break
rs = [' '.join(js[0]),
      ' '.join(js[1]),
      ' '.join(js[2]),
      ' '.join(js[3]),
      ' '.join(js[4]),
      ' '.join(js[5]),
      ' '.join(js[6]),
      ' '.join(js[7]),
      ' '.join(js[8]),
      ' '.join(js[9]),
      ' '.join(js[10]),
      ' '.join(js[11]),
      ' '.join(js[12]),
      ' '.join(js[13]),
      ' '.join(js[14]),
      ' '.join(js[15]),
      ' '.join(ps)]
res = ' '.join(rs)

ress = list(map(int, re.findall(r'\d+', res)))

rrr = [[] for _ in range(17)]
for i in range(1, 17):
    for r in ress:
        if r < 2 ** i:
            rrr[i].append(str(r))

dd = {}
for i in range(1, 17):
    dd[i] = ' '.join(rrr[i])

for _ in range(int(input())):
    print(dd[int(input())])
