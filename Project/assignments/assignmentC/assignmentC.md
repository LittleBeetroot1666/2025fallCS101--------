# Assignment #C: bfs & dp

Updated 1436 GMT+8 Nov 25, 2025

2025 fall, Complied by <mark>郭旭杰、化学与分子工程学院</mark>

账户：OpenJudge：25n2500011906，昵称：郭旭杰

​	    LeetCode/CodeForces/Luogu/sunnywhy/OnlineJudge：LittleBeetroot



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。

​	由于不可抗因素(OpenJudge平台无法连接)，本人可能无法按时完成OpenJudge上的题目，本次作业多做三道sunnywhy上的题目作为补偿，落下的OpenJudge题目将于下次提交作业时一同补齐，敬请谅解。

![局部截取_20251202_062003](D:\腾讯电脑管家截图文件\局部截取_20251202_062003.png)



## 1. 题目

### sy321迷宫最短路径

bfs, hashing, https://sunnywhy.com/sfbj/8/2/321

耗时：3h

思路：bfs类型的题目对思维能力和抽象能力有较强的要求，以下是我在充分思考并查阅有关文献后得到的解题思路：

![fc376f4c412a731ae0e618047d3831b7](C:\Users\Lenovo\Documents\xwechat_files\wxid_mhygq19nbrsk22_cecf\temp\RWTemp\2025-12\7714309b92b9d1ff7cc8082cd59b475f\fc376f4c412a731ae0e618047d3831b7.jpg)

如图所示，1为墙壁，0为平地。

![47b65bfa321ee91d37851a64da5f6f77](C:\Users\Lenovo\Documents\xwechat_files\wxid_mhygq19nbrsk22_cecf\temp\RWTemp\2025-12\7714309b92b9d1ff7cc8082cd59b475f\47b65bfa321ee91d37851a64da5f6f77.jpg)

我们可以想象有一支由很多人组成的探险队从（0,0）出发探索未知的迷宫，有些时候有不同的方向可以走就会兵分多路。但是为了避免迷路，他们每次都会用蓝色箭头标记一下自己的行进方向，直到迷宫的每一个可以探索的方格都被探索且仅被探索1次为止。

在我的解法中，我用一个字典(哈希表)来表示所有的蓝色箭头，从而实现回溯过程。

![993257841571851f17324c8e063f8e0d](C:\Users\Lenovo\Documents\xwechat_files\wxid_mhygq19nbrsk22_cecf\temp\RWTemp\2025-12\7714309b92b9d1ff7cc8082cd59b475f\993257841571851f17324c8e063f8e0d.jpg)

数据确保最终一定会有队员找到位于右下角的迷宫出口，此时他们只要逆着蓝色箭头行进就一定可以回到起点，且由于走最短路线的分队会率先到达并“占领”终点，故其必然走最短路径。

但是从起点顺着蓝色箭头不一定可以到达终点，找到出口的队员为了让位于起点的大部队找到通达终点的最短路径，应该一边往回走一边用如图所示的黄色箭头做标记，确定唯一最短路径(代码中用ress = res[::-1]表示)。

最后逆黄色箭头而行即为所求结果，注意行列的序号均要加一。



代码：

```python
import sys

dir4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve():
    n, m = list(map(int, sys.stdin.readline().split()))
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    fa = {}

    def bfs(i, j):
        if matrix[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            for di, dj in dir4:
                if 0 <= i + di <= n - 1 and 0 <= j + dj <= m - 1:
                    if matrix[i + di][j + dj] == 0 and not visited[i + di][j + dj]:
                        fa[(i + di, j + dj)] = (i, j)
                    bfs(i + di, j + dj)

    bfs(0, 0)

    res = [(n - 1, m - 1)]
    while (0, 0) not in res:
        res.append(fa[res[-1]])
    ress = res[::-1]
    for r in ress:
        print(r[0] + 1, r[1] + 1)


if __name__ == '__main__':
    solve()

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251202_052923](D:\腾讯电脑管家截图文件\局部截取_20251202_052923.png)

![局部截取_20251202_053001](D:\腾讯电脑管家截图文件\局部截取_20251202_053001.png)



### sy324多终点迷宫问题

bfs, https://sunnywhy.com/sfbj/8/2/324

耗时：30min

思路：在sy320的代码中小修小补就可以了。



代码：

```python
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

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251202_150539](D:\腾讯电脑管家截图文件\局部截取_20251202_150539.png)



### 189A. Cut Ribbon

brute force/dp, 1300, https://codeforces.com/problemset/problem/189/A

耗时：30min

思路：整体上用暴力求解，算法上属于dp中的简单类型，但是要进行分类讨论否则当a, b, c中有0的时候会爆栈。

负数对应的base值要足够小(例如:-10000)，否则会WA。



代码：

```python
from functools import lru_cache
import sys
sys.setrecursionlimit(180000)


n0, a0, b0, c0 = list(map(int, input().split()))


@lru_cache(maxsize=None)
def dp(n, a, b, c):
    if n < 0:
        return -10000
    elif n == 0:
        return 0
    else:
        return max(dp(n - a, a, b, c) + 1, dp(n - b, a, b, c) + 1, dp(n - c, a, b, c) + 1)


if n0 % min(a0, b0, c0) == 0:
    print(n0 // min(a0, b0, c0))
else:
    print(dp(n0, a0, b0, c0))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251202_061342](D:\腾讯电脑管家截图文件\局部截取_20251202_061342.png)

![局部截取_20251202_061358](D:\腾讯电脑管家截图文件\局部截取_20251202_061358.png)



### M02945:拦截导弹

dp, greedy http://cs101.openjudge.cn/pctbook/M02945

耗时：1h

思路：直接brute force查询所有子集会爆内存。

应该使用dp，用ts列表储存从每一个导弹开始拦截所能够拦截的最大导弹数量，最后输出总共可以拦截的最大导弹数量。



代码：

```python
k = int(input())
js = list(map(int, input().split()))
ts = [[j, 1] for j in js]
for i in range(1, k + 1):
    spl = [0]
    for t in range(k - i + 1, k):
        if ts[t][0] <= ts[k - i][0]:
            spl.append(ts[t][1])
        ts[k - i][1] = max(spl) + 1

res = [t[1] for t in ts]
print(max(res))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251202_160006](D:\腾讯电脑管家截图文件\局部截取_20251202_160006.png)

![局部截取_20251202_160019](D:\腾讯电脑管家截图文件\局部截取_20251202_160019.png)



### M01384: Piggy-Bank

dp, http://cs101.openjudge.cn/practice/01384/

耗时：2h

思路：dp思路与189A.Cut Ribbon类似，很有难度。

我自己照着189A.Cut Ribbon的代码来写，结果一直TLE。

腾讯元宝提供的思路：这里使用了不断维护和更新dp数组的思路，如果可以达到，则dp[w]的值不是正无穷。这样时间复杂度降低到了O(n)。

这种思路并不是像传统方法一样从p,w开刀，而是运用逆向思维，反其道而行之；看似piget比p和w都大，实则却化虚为实，化递归为迭代，变“小而深”为“大而浅”，非常巧妙。



代码：

```python
for _ in range(int(input())):
    e, f = list(map(int, input().split()))
    piget = f - e
    mat = []
    for _ in range(int(input())):
        p, w = list(map(int, input().split()))
        mat.append((p, w))

    dp = [float('inf') for _ in range(piget + 1)]
    dp[0] = 0

    for p, w in mat:
        for i in range(w, piget + 1):
            dp[i] = min(dp[i], dp[i - w] + p)

    res = dp[piget]
    if res == float('inf'):
        print("This is impossible.")
    else:
        print(f'The minimum amount of money in the piggy-bank is {res}.')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251202_174051](D:\腾讯电脑管家截图文件\局部截取_20251202_174051.png)

![局部截取_20251202_174100](D:\腾讯电脑管家截图文件\局部截取_20251202_174100.png)



### LC136:只出现一次的数字

math, https://leetcode.cn/problems/single-number/submissions/682165014/

耗时：5min

思路：使用异或^操作，极大地简化了代码，节省了运行时间。



代码：

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for i in nums:
            n = n ^ i
        return n
        
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251202_162628](D:\腾讯电脑管家截图文件\局部截取_20251202_162628.png)



### sy318数字操作

math, brute force, dfs https://sunnywhy.com/sfbj/8/2/318

耗时：5min

思路：逆向思维，从大数出发，能除以二就除以二，除不尽就减一，直到得到1为止。



代码：

```python
n = int(input())
cnt = 0
while n != 1:
    if n % 2 == 0:
        n //= 2
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251202_063345](D:\腾讯电脑管家截图文件\局部截取_20251202_063345.png)



### sy319矩阵中的块

dfs https://sunnywhy.com/sfbj/8/2/319

耗时：30min

思路：类似OpenJudge上的鱼塘个数问题，都是通过dfs找连通块的个数。



代码：

```python
dir4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cnt = 0


def visitable(i, j):
    if 0 <= i <= n - 1 and 0 <= j <= m - 1 and matrix[i][j] == 1:
        return True
    else:
        return False
        
        
n, m = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]


def dfs(i, j):
    if visitable(i, j) and not visited[i][j]:
        visited[i][j] = True
        for di, dj in dir4:
            dfs(i + di, j + dj)


for i0 in range(n):
    for j0 in range(m):
        if matrix[i0][j0] == 1 and not visited[i0][j0]:
            cnt += 1
            dfs(i0, j0)

print(cnt)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251202_063542](D:\腾讯电脑管家截图文件\局部截取_20251202_063542.png)



### sy320迷宫问题

bfs, deque https://sunnywhy.com/sfbj/8/2/320

耗时：2h30min

思路：从起点出发，每次遍历相邻的格子，记录次数cnt，如果到达终点，立即停止遍历，输出cnt；如果队列已经被清空仍无法到达终点，输出-1即可。

第一次使用queue，十分生疏~



代码：

```python
import sys
from collections import deque

dir4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs():
    n, m = list(map(int, sys.stdin.readline().split()))
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    cnt = 0
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        lq = len(queue)
        for _ in range(lq):
            i, j = queue.popleft()
            if i == n - 1 and j == m - 1:
                return cnt
            for di, dj in dir4:
                if 0 <= i + di <= n - 1 and 0 <= j + dj <= m - 1:
                    if matrix[i + di][j + dj] == 0 and not visited[i + di][j + dj]:
                        visited[i + di][j + dj] = True
                        queue.append((i + di, j + dj))
        cnt += 1
    
    return -1

print(bfs())

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251202_144231](D:\腾讯电脑管家截图文件\局部截取_20251202_144231.png)



## 2. 学习总结和收获

前几天我想尝试自己把题目做出来，结果被题目吓到了，怎么都没有思路；

最后又是查看题解，又是求助AI，又是运行PythonTutor找代码错误，这几道题做了我一宿。

bfs对于我来说还是有很大的难度的，而且很多时候bfs与dfs容易混为一谈。

dp继续对数学高要求，难度总体较高。

但是在做dp题目的时候，最好只要有了一个思路，哪怕是再笨的方法，都要敢于尝试，没准能AC。

做题看看题目标签还是很有用的，但是针对实战情况，灵活地选择策略(greedy,dp,dfs,bfs)需要经验的积累。

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

我参加了周四的学校周测，最终AC3，OpenJudge上最好Python和Pypy都提交一遍，否则有些题目会出现只有Python能通过或只有Pypy能通过的Bug~。

让我非常有成就感的是我独立完成了第一题dfs和第三题dp的程序编写，以前编写dfs和dp或多或少都要看题解。

![局部截取_20251202_143331](D:\腾讯电脑管家截图文件\局部截取_20251202_143331.png)

![局部截取_20251202_143906](D:\腾讯电脑管家截图文件\局部截取_20251202_143906.png)

![局部截取_20251202_143340](D:\腾讯电脑管家截图文件\局部截取_20251202_143340.png)

![局部截取_20251202_143351](D:\腾讯电脑管家截图文件\局部截取_20251202_143351.png)

![局部截取_20251202_143515](D:\腾讯电脑管家截图文件\局部截取_20251202_143515.png)

![局部截取_20251202_143524](D:\腾讯电脑管家截图文件\局部截取_20251202_143524.png)

![局部截取_20251202_143457](D:\腾讯电脑管家截图文件\局部截取_20251202_143457.png)

![局部截取_20251202_143507](D:\腾讯电脑管家截图文件\局部截取_20251202_143507.png)

![局部截取_20251202_143906](D:\腾讯电脑管家截图文件\局部截取_20251202_143906.png)



周五晚上参加CodeForces [Educational Codeforces Round 185 (Rated for Div. 2)](https://codeforces.com/contest/2170)最终AC2

![局部截取_20251202_054625](D:\腾讯电脑管家截图文件\局部截取_20251202_054625.png)



周六晚上参加CodeForces [Codeforces Round 1067 (Div. 2)](https://codeforces.com/contest/2158) 最终AC1

![局部截取_20251202_054750](D:\腾讯电脑管家截图文件\局部截取_20251202_054750.png)



周日上午又参加了LeetCode 周赛 [第 478 场周赛](https://leetcode.cn/contest/weekly-contest-478) AC2 得8分 1112名

![局部截取_20251202_055032](D:\腾讯电脑管家截图文件\局部截取_20251202_055032.png)

![局部截取_20251130_121246](D:\腾讯电脑管家截图文件\局部截取_20251130_121246.png)



周日下午参加计概小班课并做题练习

![局部截取_20251202_060954](D:\腾讯电脑管家截图文件\局部截取_20251202_060954.png)

![WeChatAppEx.exe_20251202_060929](D:\腾讯电脑管家截图文件\WeChatAppEx.exe_20251202_060929.png)

![局部截取_20251202_061103](D:\腾讯电脑管家截图文件\局部截取_20251202_061103.png)
