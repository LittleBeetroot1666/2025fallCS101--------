n = int(input())
ds = list(map(int, input().split()))
a, b = list(map(int, input().split()))
print(sum(ds[a - 1: b - 1]))
