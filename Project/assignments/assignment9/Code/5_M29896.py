x, n = list(map(int, input().split()))
js = list(map(int, input().split()))
# 输入数据

if 1 not in js:
    print('-1')
# 只有一种情况，即没有一元硬币时，会由于凑不出一元面值而不可能实现

else:
    js.sort(reverse=True)    # 倒序方便接下来找最大值（贪心）
    now_max = 0        # 现在持有的硬币最多可以全部表示从1到now_max的所有数
    cnt = 0            # 需要的硬币总数为cnt

    while now_max < x:
        for j in js:
            if j <= now_max + 1:
                now_max += j    # 贪心：找不大于now_max + 1的最大面额硬币，
# 这样能确保不存在不能被表示的数字。
                cnt += 1
                break    # 确保每次都对所有硬币面额从大到小梳理。
    print(cnt)
