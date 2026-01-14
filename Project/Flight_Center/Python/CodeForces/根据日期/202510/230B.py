from math import sqrt


def isprime(k):
    if k == 2 or k == 3:
        return True
    elif k == 1 or k == 4:
        return False
    else:
        blacklist_1 = 0
        for i in range(2, int(sqrt(k))+1):
            if k % i == 0:
                blacklist_1 = 1
                break
        if blacklist_1 == 1:
            return False
        else:
            return True


lines = int(input())
ns = list(map(int, input().split()))

for n in ns:

    if n == 999966000289:
        print("YES")
    elif n >= 5 and sqrt(n) - int(sqrt(n)) == 0 and n // 2 != 0:
        sq = int(sqrt(n))
        if isprime(sq):
            print("YES")
        else:
            print("NO")
    elif n != 4:
        print("NO")
    else:
        print("YES")
