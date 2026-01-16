sx = [-2, -1, 1, 2, 2, 1, -1, -2]
sy = [1, 2, 2, 1, -1, -2, -2, -1]

cnt = 0


def dfs(dep, x0, y0):
    if n * m == dep:
        global cnt
        cnt += 1
        return

    for r in range(8):
        xt = x0 + sx[r]
        yt = y0 + sy[r]
        if chess[xt][yt] is False and 0 <= xt < n and 0 <= yt < m:
            chess[xt][yt] = True
            dfs(dep + 1, xt, yt)
            chess[xt][yt] = True
            dfs(dep + 1, xt, yt)
            # 下面一行代码不容易理解，模拟一下可以发现，这行代码当且仅当所有方向都走不通时执行，其作用是退回到上一步，即回溯。
            chess[xt][yt] = False


for _ in range(int(input())):   # Lne表达的极简版
    n, m, x, y = list(map(int, input().split()))
    chess = [[False] * 10 for _ in range(10)]
    # False表示没有走过，由于棋盘的范围在函数中已经敲定，故chess的内容可以尽可能大一些。
    cnt = 0
    chess[x][y] = True    # 起点不能重复经过，记为True
    dfs(1, x, y)
    print(cnt)
