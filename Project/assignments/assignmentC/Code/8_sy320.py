import sys
from collections import deque

dir4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs():
    n, m = list(map(int, sys.stdin.readline().split()))
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    cnt = 0
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        lq = len(queue)
        for _ in range(lq):
            i, j = queue.popleft()
            if i == n - 1 and j == m - 1:
                return cnt
            for di, dj in dir4:
                if 0 <= i + di <= n - 1 and 0 <= j + dj <= m - 1:
                    if matrix[i + di][j + dj] == 0 and not visited[i + di][j + dj]:
                        visited[i + di][j + dj] = True
                        queue.append((i + di, j + dj))
        cnt += 1

    return -1


print(bfs())
