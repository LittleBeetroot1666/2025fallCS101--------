dir_horse = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

for _ in range(int(input())):  # Lne表达的极简版
    n, m, x, y = list(map(int, input().split()))
    visited = [[False] * m for _ in range(n)]
    cnt = [0]

    def dfs(dep, x0, y0):
        if n * m == dep:
            cnt[0] += 1
            return

        for i in range(len(dir_horse)):
            xt = x0 + dir_horse[i][0]
            yt = y0 + dir_horse[i][1]
            if 0 <= xt < n and 0 <= yt < m and not visited[xt][yt]:
                visited[xt][yt] = True
                dfs(dep + 1, xt, yt)
                # 下面一行代码不容易理解，模拟一下可以发现，这行代码当且仅当所有方向都走不通时执行，其作用是退回到上一步，即回溯。
                visited[xt][yt] = False

    visited[x][y] = True    # 起点不能重复经过，记为True
    dfs(1, x, y)
    print(cnt[0])
