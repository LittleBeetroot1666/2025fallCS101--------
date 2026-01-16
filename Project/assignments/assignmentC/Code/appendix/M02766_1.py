n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# 计算每行的前缀和
prefix = [[0] * (n + 1) for _ in range(n)]
for i in range(n):
    for j in range(1, n + 1):
        prefix[i][j] = prefix[i][j - 1] + matrix[i][j - 1]

max_sum = -float('inf')

# 遍历所有可能的列区间i到j
for i in range(1, n + 1):
    for j in range(i, n + 1):
        # 当前列区间i..j，计算每行的和，形成一个一维数组temp
        temp = []
        for k in range(n):
            current_sum = prefix[k][j] - prefix[k][i - 1]
            temp.append(current_sum)

        # 使用Kadane算法找temp中的最大子数组和
        if not temp:
            continue
        current_max = temp[0]
        global_max = temp[0]
        for num in temp[1:]:
            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)

        if global_max > max_sum:
            max_sum = global_max

print(max_sum)
