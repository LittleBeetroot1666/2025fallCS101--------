a, b = list(map(int, input().split()))
c = max(a, b) - min(a, b)
print(min(a, b), c // 2)
