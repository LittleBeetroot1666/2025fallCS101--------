for _ in range(int(input())):
    k = int(input())
    if k % 2 != 0 or k <= 0:
        print(0)
    else:
        print(k // 4 + 1)
