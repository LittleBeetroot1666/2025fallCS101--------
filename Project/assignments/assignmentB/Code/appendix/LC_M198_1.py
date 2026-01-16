def rob(nums):
    res = []

    def dfs(index, current_sum):
        # 终止条件：索引超出房屋范围时，将当前金额加入结果
        if index >= len(nums):
            res.append(current_sum)
            return
        # 选择偷窃当前房屋，跳过下一间房屋
        dfs(index + 2, current_sum + nums[index])
        # 选择不偷窃当前房屋，继续考虑下一间房屋
        dfs(index + 1, current_sum)

    # 从第0间房屋开始递归，初始金额为0
    dfs(0, 0)
    res.sort(reverse=True)
    return res[0]
