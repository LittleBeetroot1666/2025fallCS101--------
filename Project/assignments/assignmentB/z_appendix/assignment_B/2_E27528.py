js = [1]
for _ in range(25):
    js.append(sum(js) + 1)

n = int(input())
print(js[n - 1])
