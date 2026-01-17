n, D = map(int, input().split())
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
