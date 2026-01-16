from math import sqrt

sq2 = sqrt(2)
Lne = int(input())
for _ in range(Lne):
    n = int(input())
    ng1 = (sq2 + 1) ** n - (1 - sq2) ** n
    res = int(ng1 // (2 * sq2)) + 1
    resr = int(res) % 32767
    print(resr)
