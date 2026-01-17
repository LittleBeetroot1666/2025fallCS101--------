n, m, a = list(map(int, input().split()))
if n % a != 0:
    l = n // a + 1
else:
    l = n // a
if m % a != 0:
    w = m // a + 1
else:
    w = m // a
print(l * w)
