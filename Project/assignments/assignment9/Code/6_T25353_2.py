# 我的代码（自己写的注释），应该正确，但是会严重超时
n, d = list(map(int, input().split()))
js = []
for i in range(n):
    j = int(input())
    js.append([j, i])
# 输入队列中所有人的身高和初始状态的序号
for i in range(n):
    pas = 0
    # pas变量表示这位同学最多还能往前排的位数
    while i - 1 - pas >= 0 and abs(js[i - 1 - pas][0] - js[i][0]) <= d:
        pas += 1
    # 求出pas的值
    if pas >= 1:
        for t in range(i - pas, i):
            if js[t][0] > js[i][0]:
                js[i][1] = js[t][1]
                # 如果后面同学的身高较低就尽可能往前面站
                for g in range(t, i):
                    js[g][1] += 1
                # 队列先不动，只是改变序号
                break

    js.sort(key=lambda x: x[1])
    # 按照序号重新排队，此时就能得到身高的字典序最小的队列
for j in js:
    print(j[0])
# 从前往后依次报出每一位同学的身高
