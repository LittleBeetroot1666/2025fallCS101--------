n, k, l, c, d, p, nl, np = list(map(int, input().split()))
js = [k * l // (n * nl), c * d // n, p // (n * np)]
print(min(js))
