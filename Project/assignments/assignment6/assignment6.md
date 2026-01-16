# Assignment #6: 矩阵、贪心

Updated 1432 GMT+8 Oct 14, 2025

2025 fall, Complied by <mark>同学的姓名、院系</mark>



>**说明：**
>
>1. **解题与记录：**
>
>  对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. 提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### M18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/pctbook/M18211

耗时：20min通过

思路：基础的双指针问题，需要贪心算法。

首先判定鸣人是否能买得起最便宜的武器，如果买不起直接输出0。

如果买得起最便宜的武器，鸣人先按价格由低到高尽可能多地买入便宜的武器，然后反复执行卖掉最贵的一种武器并用所得的钱按照价格由低到高依次买入最便宜的武器，直到剩下0或1种武器终止，即可得到正确结果。

代码

```python
# Python,two pointers,greedy
p = int(input())
js = list(map(int, input().split()))
js.sort()
jsr = []
for _ in range(1,len(js)+1):
    jsr.append(js[-_])

lt = len(js)
if p < js[0]:
    print(0)
else:
    a = b = 0
    a += 1
    p -= js[0]
    dta = 1
    while a + b < lt:
        while p >= js[a]:
            p -= js[a]
            a += 1
            dta += 1
        if jsr[b] >= js[a]:
            p += jsr[b] - js[a]
            a += 1
            b += 1

    print(dta)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251016_002320](D:\腾讯电脑管家截图文件\局部截取_20251016_002320.png)

![局部截取_20251016_002340](D:\腾讯电脑管家截图文件\局部截取_20251016_002340.png)

### M21554: 排队做实验

greedy, http://cs101.openjudge.cn/pctbook/M21554/

耗时：1h左右才通过。

思路：取材于经典数学问题("水桶打水最优策略")，这种先处理小问题的策略在经济管理上有广泛应用。

需要灵活运用矩阵知识



代码

```python
n = int(input())
js = list(map(int, input().split()))
js1 = []
sq = []
for i in range(n):
    sq.append([js[i],i])
sq.sort()

for i in range(n):
    js1.append(sq[i][1]+1)
print(" ".join(map(str,js1)))

sgm = 0
su = 0
js.sort()
for i in range(n):
    sgm += su
    su += js[i]
k_out = sgm / n
print("%.2f" % k_out)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/pctbook/E23555



思路：较难，需要强大的数学基础，个人认为应该归于M类题目。



代码

```python
n, m1, m2 = map(int, input().split())
A = [[0 for x1 in range(n)] for y1 in range(n)]
B = [[0 for x2 in range(n)] for y2 in range(n)]
C = [[0 for x3 in range(n)] for y3 in range(n)]
for i in range(m1):
    a, b, k = map(int, input().split())
    A[a][b] = k
for i in range(m2):
    a, b, k = map(int, input().split())
    B[a][b] = k
for i1 in range(n):
    for j1 in range(n):
        res = 0
        for t in range(n):
            res += A[i1][t] * B[t][j1]
        C[i1][j1] = res

for a1 in range(n):
    for b1 in range(n):
        if C[a1][b1] != 0:
            print(a1, b1, C[a1][b1])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/pctbook/M12558

耗时：15min速通

思路：这个题目思路非常简单，小学的数学内容，只需要基础的矩阵知识，只不过代码较长一些。

个人认为应该归于E类题目。



代码

```python
n, m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

C = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            C += 4

for i in range(n):
    for j in range(m-1):
        if matrix[i][j] + matrix[i][j+1] == 2:
            C -= 2

for j in range(m):
    for i in range(n-1):
        if matrix[i][j] + matrix[i+1][j] == 2:
            C -= 2

print(C)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/



思路：



代码

```python
# 用null = input()实现空行
# 贪心
# 坐标系变换

from math import sqrt

def yuntin2x(x,y,r0):
    if y <= r0:
        return x - sqrt(r0 ** 2 - y ** 2), x + sqrt(r0 ** 2 - y ** 2)
    else:
        return ()

n = 1
d = 1
cnt = 0
blacklist = 0
res = 0

while blacklist == 0:
    cnt += 1
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        blacklist = 1
        break
    ghets = []
    for _ in range(n):
        res = 0
        blacka = 0
        a, b = map(int, input().split())
        if b <= d:
            ghets.append(yuntin2x(a, b, d))
        else:
            blacka += 1
            res = -1
    null = input()

    rrest = -float('inf')
    if res == -1:
        null = 0
    else:
        ghets.sort(key=lambda x: x[1])
        for ip in ghets:
            if ip[0] > rrest:
                res += 1
                rrest = ip[1]

    print("Case "+str(cnt)+": "+str(res))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C



思路：



代码

```python
n = int(input())
trees = []
for i in range(n):
    th = list(map(int, input().split()))
    trees.append(th)

if n <= 2:
    cut = n
else:
    cut = 2
    left = trees[0][0]
    for i in range(1, n - 1):
        if trees[i][0] - trees[i][1] > left:
            cut += 1
            left = trees[i][0]
        elif trees[i][0] - trees[i][1] <= left and trees[i][0] + trees[i][1] < trees[i + 1][0]:
            cut += 1
            left = trees[i][0] + trees[i][1]
        else:
            cut += 0
            left = trees[i][0]

print(cut)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

我用矩阵给自己出了一道题，类似于小游戏的那种，可以用来巩固基础的矩阵知识。





