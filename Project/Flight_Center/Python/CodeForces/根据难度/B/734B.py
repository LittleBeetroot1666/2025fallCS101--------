js = list(map(int, input().split()))
c = min(js[0], js[2], js[3])
s = min(js[0] - c, js[1])
print(256 * c + 32 * s)
