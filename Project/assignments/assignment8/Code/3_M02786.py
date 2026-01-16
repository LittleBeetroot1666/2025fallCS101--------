pell = [0, 1]
for _ in range(1000000):
    pell.append((pell[-2] + 2 * pell[-1]) % 32767)


Lne = int(input())
for _ in range(Lne):
    print(pell[int(input())])
