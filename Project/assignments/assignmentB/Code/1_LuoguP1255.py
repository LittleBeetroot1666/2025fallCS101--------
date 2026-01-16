a = 0
b = 1
js = []
for _ in range(5000):
    a += b
    js.append(a)
    b += a
    js.append(b)

n = int(input())
print(js[n - 1])
