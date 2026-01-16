import sys


# 1. 读取所有输入，合并成一个字符串
all_input = sys.stdin.read().strip()  # 先读入全部输入，并去掉首尾空白

# 2. 按空白（空格/换行/制表符等）分割出所有数字字符，转成整数列表
num_str_list = all_input.split()
num_list = list(map(int, num_str_list))  # 转为整数

# 3. 读取第一行的 N，确定矩阵大小
n = num_list[0]
# 剩下的元素就是要组成矩阵的数字，长度应该是 n*n
matrix_elements = num_list[1:]

# 4. 检查元素数量是否匹配 N*N（题目说输入合法，可省略）
assert len(matrix_elements) == n * n, "输入元素数量与 N 不匹配"

# 5. 将一维列表切分为二维矩阵（每 N 个元素为一行）
matrix = []
for i in range(n):
    start = i * n
    end = start + n
    row = matrix_elements[start:end]
    matrix.append(row)


def max_sub_array(nums):
    cur_sum = max_sum = nums[0]
    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)
    return max_sum


n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

ans = float('-inf')
# 枚举上边界 top
for top in range(n):
    col_sum = [0] * n  # 每列的累加和
    # 枚举下边界 bottom
    for bottom in range(top, n):
        # 把 bottom 行的元素加到对应列的累加和中
        for col in range(n):
            col_sum[col] += matrix[bottom][col]
        # 对当前 col_sum 用 Kadane 算法求最大子数组和
        cur_max = max_sub_array(col_sum)
        ans = max(ans, cur_max)

print(ans)
