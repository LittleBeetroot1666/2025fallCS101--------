for _ in range(int(input())):
    n = int(input())
    y, r = list(map(int, input().split()))
    print(min(n, y // 2 + r))
