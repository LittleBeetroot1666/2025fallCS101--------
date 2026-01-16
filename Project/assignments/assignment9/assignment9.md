# Assignment #9: Mock Exam立冬前一天

Updated 1658 GMT+8 Nov 6, 2025

2025 fall, Complied by <mark>郭旭杰、化学与分子工程学院</mark>



>**说明：**
>
>1. Nov⽉考： AC4<mark>（AC4）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
>2. 解题与记录：对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>3. 提交安排：提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
>4. 延迟提交：如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



考试情况速览：

![局部截取_20251110_210807](D:\腾讯电脑管家截图文件\局部截取_20251110_210807.png)

![局部截取_20251110_210859](D:\腾讯电脑管家截图文件\局部截取_20251110_210859.png)

![局部截取_20251110_211036](D:\腾讯电脑管家截图文件\局部截取_20251110_211036.png)



## 1. 题目

### E29982:一种等价类划分问题

hashing, http://cs101.openjudge.cn/practice/29982

耗时：15min,3次尝试

思路：去逗号加逗号要熟练，基础的二维数组运用，二维数组(mkf)分行分划预留足9999防止RE。



代码

```python
def kcj(listy):
    return ','.join(listy)


m, n, k = map(int, input().split(','))
mkf = [[]for _ in range(9999)]
for i in range(m + 1, n):
    ts = i // 1000 + i % 1000 // 100 + i % 100 // 10 + i % 10
    if ts % k == 0:
        mkf[ts // k].append(str(i))

for row in mkf:
    if len(row) > 0:
        print(kcj(row))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251110_211524](D:\腾讯电脑管家截图文件\局部截取_20251110_211524.png)

![局部截取_20251110_211537](D:\腾讯电脑管家截图文件\局部截取_20251110_211537.png)



### E30086:dance

greedy, http://cs101.openjudge.cn/practice/30086

耗时：3min,1次通过

思路：简单的送分题。



代码

```python
n, d = list(map(int, input().split()))
js = list(map(int, input().split()))
js.sort()
blacklist = 0
for i in range(n):
    if js[2 * i + 1] - js[2 * i] > d:
        blacklist += 1
if blacklist > 0:
    print('No')
else:
    print('Yes')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251110_212215](D:\腾讯电脑管家截图文件\局部截取_20251110_212215.png)

![局部截取_20251110_212224](D:\腾讯电脑管家截图文件\局部截取_20251110_212224.png)



### M25570: 洋葱

matrices, http://cs101.openjudge.cn/practice/25570

耗时：24min,9次尝试

思路：就是一层一层地剥洋葱直到剥完。

可以使用迭代或者递归，这里由于n已经给出，使用迭代（for循环）更方便易行。但是无论是那种方法都应该将最后两层单独讨论。

注意参数的取值等细节，时间大多耗在这些细节上。



代码

```python
def sgm_skin(amatrix):
    if len(amatrix) == 1:
        return amatrix[0][0]
    elif len(amatrix) == 2:
        return amatrix[0][0] + amatrix[0][1] + amatrix[1][0] + amatrix[1][1]
    else:
        k0 = 0
        k0 += sum(amatrix[0])
        k0 += sum(amatrix[-1])
        for _ in range(1, len(amatrix) - 1):
            k0 += amatrix[_][0]
            k0 += amatrix[_][-1]
        return k0

def peel(amatrix):
    if len(amatrix) <= 2:
        return [[]]
    elif len(amatrix) == 3:
        return [[amatrix[1][1]]]
    else:
        new_amatrix = []
        for _ in range(1, len(amatrix) - 1):
            new_amatrix.append(amatrix[_][1:len(amatrix[_]) - 1])
        return new_amatrix


n = int(input())
js = []
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
js.append(sgm_skin(matrix))
for j in range((n - 1)//2):
    matrix = peel(matrix)
    js.append(sgm_skin(matrix))

print(max(js))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251110_212915](D:\腾讯电脑管家截图文件\局部截取_20251110_212915.png)

![局部截取_20251110_212931](D:\腾讯电脑管家截图文件\局部截取_20251110_212931.png)



### M28906:数的划分

dfs, dp, http://cs101.openjudge.cn/practice/28906

耗时：16min,1次通过


思路：典型的递归问题，有一定难度，要先在草稿纸上理清数学问题的思路再落实到代码上。



代码

```python
def div(n0, k0):
    if k0 == 2:
        return n0 // 2
    else:
        res = 0
        i = 0
        while n0 - i * k0 - 1 >= 2:
            res += div(n0 - i * k0 - 1, k0 - 1)
            i += 1
        return res
    
n, k = map(int, input().split())
print(div(n, k))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251110_213514](D:\腾讯电脑管家截图文件\局部截取_20251110_213514.png)

![局部截取_20251110_213530](D:\腾讯电脑管家截图文件\局部截取_20251110_213530.png)



### M29896:购物

greedy, http://cs101.openjudge.cn/practice/29896

耗时：写了半个下午和一整个晚上，最后求助AI并在群里讨论，最终写出了自己的题解。

思路：硬币面额从小到大凑，但是较大面额的硬币面额尽量大，这样才能使硬币总数最少，这体现了贪心算法思想。



代码

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251110_212109](D:\腾讯电脑管家截图文件\局部截取_20251110_212109.png)

![局部截取_20251110_212826](D:\腾讯电脑管家截图文件\局部截取_20251110_212826.png)

![局部截取_20251110_212119](D:\腾讯电脑管家截图文件\局部截取_20251110_212119.png)



### T25353:排队

greedy, http://cs101.openjudge.cn/practice/25353

耗时：写了大半个下午，最后不得不阅读题解。

思路：早就听说这一题排队特别难，这次终于可以会会它了，没想到我做不出来（TLE），求助AI结果现在几乎所有的AI(腾讯云宝，DeepSeek，豆包，夸克)也做不出来（WA）。最后还是看了老师提供的题解，有向无环图比较令人费解。

代码

自己的（TLE）

```Python
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

```

题解提供（AC）

```python
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

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251110_212007](D:\腾讯电脑管家截图文件\局部截取_20251110_212007.png)

![局部截取_20251110_212029](D:\腾讯电脑管家截图文件\局部截取_20251110_212029.png)

![局部截取_20251110_212351](D:\腾讯电脑管家截图文件\局部截取_20251110_212351.png)



## 2. 学习总结和收获

这次拿到AC4，较上次有进步，但是解决难题的能力还有待提高。

如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。

本周期中周，我除参加月考外还参加了化学安全、英语、高等数学的考试，额外练习就很少。

周日考完数学后回寝室参加了LeetCode的第475场周赛，明显比上周的那场难，只能做出第一题，第二题题面和第一题一样，但是数据更大，我就一直TLE，后两题也没有做出来，不是很理想。

![局部截取_20251109_120556](D:\腾讯电脑管家截图文件\局部截取_20251109_120556.png)

