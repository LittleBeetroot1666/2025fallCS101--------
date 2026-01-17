primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
Lne = int(input())
for _ in range(Lne):
    n = int(input())
    js = list(map(int, input().split()))
    if min(js) == 1:
        print(2)
    else:
        cnt = 0
        blacklist = 0
        while blacklist == 0:
            for j in js:
                if j % primes[cnt] != 0:
                    blacklist = 1
                    break
            if blacklist == 0:
                for i in range(len(js)):
                    js[i] //= primes[cnt]
                cnt += 1
        print(primes[cnt])
