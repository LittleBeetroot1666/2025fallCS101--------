import sys
from collections import deque


def kpj(listy):
    return ' '.join(listy)


def matrix_out_print(amatrix):
    for arow in amatrix:
        print(kpj(arow))


dir4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve():
    def to_get_mig():
        n, m = list(map(int, sys.stdin.readline().split()))
        matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        mig = [['-1' for _ in range(m)] for _ in range(n)]

        cnt = 0
        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            lq = len(queue)
            for _ in range(lq):
                i, j = queue.popleft()
                mig[i][j] = str(cnt)
                for di, dj in dir4:
                    if 0 <= i + di <= n - 1 and 0 <= j + dj <= m - 1:
                        if matrix[i + di][j + dj] == 0 and not visited[i + di][j + dj]:
                            queue.append((i + di, j + dj))
                            visited[i + di][j + dj] = True
            cnt += 1

        return mig

    matrix_out_print(to_get_mig())


if __name__ == '__main__':
    solve()
