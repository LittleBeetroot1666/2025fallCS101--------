for _ in range(int(input())):
    e, f = list(map(int, input().split()))
    piget = f - e
    mat = []
    for _ in range(int(input())):
        p, w = list(map(int, input().split()))
        mat.append((p, w))

    dp = [float('inf') for _ in range(piget + 1)]
    dp[0] = 0

    for p, w in mat:
        for i in range(w, piget + 1):
            dp[i] = min(dp[i], dp[i - w] + p)

    res = dp[piget]
    if res == float('inf'):
        print("This is impossible.")
    else:
        print(f'The minimum amount of money in the piggy-bank is {res}.')
