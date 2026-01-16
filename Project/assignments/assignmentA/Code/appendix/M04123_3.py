import sys

# 马的8种可能的移动方向（dx, dy）
directions = [(2, 1), (1, 2), (-1, 2), (-2, 1),
              (-2, -1), (-1, -2), (1, -2), (2, -1)]


Lne = int(sys.stdin.readline())  # 读取测试用例数
for _ in range(Lne):
    n, m, x, y = map(int, sys.stdin.readline().split())  # 棋盘大小n*m，初始位置(x,y)
    visited = [[False] * m for _ in range(n)]  # 记录格子是否已访问
    count = [0]  # 用列表存储结果，以便在递归中修改

    def dfs(current_x, current_y, step):
        # 终止条件：已遍历完所有n*m个格子
        if step == n * m:
            count[0] += 1
            return
        # 尝试8种移动方向
        for dx, dy in directions:
            next_x = current_x + dx
            next_y = current_y + dy
            # 检查下一个位置是否合法（在棋盘内且未被访问）
            if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]:
                visited[next_x][next_y] = True  # 标记为已访问
                dfs(next_x, next_y, step + 1)  # 递归进入下一步
                visited[next_x][next_y] = False  # 回溯，取消标记

    visited[x][y] = True  # 标记初始位置为已访问
    dfs(x, y, 1)  # 初始步数为1（已走过初始位置）
    print(count[0])
