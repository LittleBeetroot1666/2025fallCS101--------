dir4 = [[-1, 0], [1, 0], [0, -1], [0, 1]]   # 四方
amatrix = [[]]  # 预处理，更美观实用


def dfs(x0, y0, tara):
    amatrix[x0][y0] = '0'
    for i0 in range(len(dir4)):
        xt = x0 + dir4[i0][0]
        yt = y0 + dir4[i0][1]
        if amatrix[xt][yt] == tara:
            dfs(xt, yt, tara)


for _ in range(int(input())):   # Lne输入的简化版本
    n = int(input())
    amatrix = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    # 先生成矩阵，接下来直接填，很爽很简洁的代码

    for i in range(1, n + 1):
        amatrix[i][1: -2] = input()

    red = 0
    black = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if amatrix[i][j] == 'r':
                dfs(i, j, 'r')      # 直接调用
                red += 1
            elif amatrix[i][j] == 'b':
                dfs(i, j, 'b')
                black += 1

    print(red, black)
