# 25353: 排队
# 题意：每次只能交换相邻且身高差不超过 D 的人，求字典序最小的最终排列
# 思路：将允许交换关系看作有向无环图（DAG），每次取“入度为 0”的人中身高最小者输出。
# 实现：多轮扫描——每轮找出当前所有入度为 0 的节点集合 S，
#       对 S 内按身高升序输出并从序列中删除，重复直到序列为空。
# 注意：最坏情况下复杂度为 O(N^2)。

import sys
input = sys.stdin.readline


def solve():
    line = input().split()
    if not line:
        return
    n, D = map(int, line)
    arr = [int(input()) for _ in range(n)]

    result = []
    cur = arr[:]  # 当前剩余队列

    while cur:
        m = len(cur)
        S_idx = []  # 当前入度为 0 的位置下标
        left_min = None
        left_max = None

        for i in range(m):
            h = cur[i]
            if i == 0:
                # 第一个人必然没有左侧约束，入度为 0
                S_idx.append(i)
                left_min = h
                left_max = h
                continue

            # 判断是否满足：与左侧所有人身高差均 ≤ D
            # 即 h 必须位于 [left_max - D, left_min + D] 区间内
            if left_max - D <= h <= left_min + D:
                S_idx.append(i)

            # 更新左侧区间最小/最大值
            if h < left_min:
                left_min = h
            if h > left_max:
                left_max = h

        # 收集并按身高升序排序
        S = [cur[i] for i in S_idx]
        S.sort()

        # 输出这些人
        result.extend(S)

        # 删除已输出的元素（保持原相对顺序）
        to_remove = set(S_idx)
        cur = [cur[i] for i in range(m) if i not in to_remove]

    # 输出结果
    print('\n'.join(map(str, result)))


if __name__ == "__main__":
    solve()
