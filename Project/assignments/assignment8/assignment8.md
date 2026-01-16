# Assignment #8: 递归

Updated 1315 GMT+8 Oct 21, 2025

2025 fall, Complied by <mark>郭旭杰、化学与分子工程学院</mark>



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

### M04147汉诺塔问题(Tower of Hanoi)

dfs, http://cs101.openjudge.cn/pctbook/M04147

耗时：30min解决（上课讲了很大一部分了）

思路：基础的递归，经典问题。



代码

```python
def mov_hanoi(n0, a0, b0):
    return f'{n0}:{a0}->{b0}'


def solv_hanoi(n0, a0, b0, c0):
    if n0 == 1:
        return [mov_hanoi(n0, a0, c0)]
    else:
        jit_sp_solv_hanoi = []
        for i in solv_hanoi(n0 - 1, a0, c0, b0):
            jit_sp_solv_hanoi.append(str(i))
        jit_sp_solv_hanoi.append(mov_hanoi(n0, a0, c0))
        for i in solv_hanoi(n0 - 1, b0, a0, c0):
            jit_sp_solv_hanoi.append(str(i) )
        return jit_sp_solv_hanoi


n, a, b, c = list(map(str,input().split()))
n_int = int(n)
js = solv_hanoi(n_int, a, b, c)
for j in js:
    print(j)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251103_005557](D:\腾讯电脑管家截图文件\局部截取_20251103_005557.png)

![局部截取_20251103_005605](D:\腾讯电脑管家截图文件\局部截取_20251103_005605.png)



### M05585: 晶矿的个数

matrices, dfs similar, http://cs101.openjudge.cn/pctbook/M05585

耗时：整理思路耗时数日，改代码做了我大半个晚上。

思路：用到了dfs，学起来有难度。

最终求助腾讯元宝，提供了一个双矩阵映射的思路。我对其加以完善。

我自己的思路是使用三维数组，但是最终没有成功。



代码

```python
def kpj(listy):
    return ' '.join(listy)


Lne = int(input())
for _ in range(Lne):
    n = int(input())
    visited = [[False] * n for _ in range(n)]
    matrix = []
    for i in range(n):
        row = []
        row_root = input()
        for rr0 in row_root:
            row.append(rr0)
        matrix.append(row)
    red = 0
    black = 0

    def dfs_pm(i0, j0, tara):
        if i0 < 0 or i0 >= n or j0 < 0 or j0 >= n:
            return
        if visited[i0][j0]:
            return
        if matrix[i0][j0] != tara:
            return
        visited[i0][j0] = True
        dfs_pm(i0 + 1, j0, tara)
        dfs_pm(i0 - 1, j0, tara)
        dfs_pm(i0, j0 + 1, tara)
        dfs_pm(i0, j0 - 1, tara)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'r' and not visited[i][j]:
                red += 1
                dfs_pm(i, j, 'r')
            elif matrix[i][j] == 'b' and not visited[i][j]:
                black += 1
                dfs_pm(i, j, 'b')

    print(red, black)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251103_005322](D:\腾讯电脑管家截图文件\局部截取_20251103_005322.png)

![局部截取_20251103_005334](D:\腾讯电脑管家截图文件\局部截取_20251103_005334.png)



### M02786: Pell数列

dfs, dp, http://cs101.openjudge.cn/pctbook/M02786/

耗时：几天内不断优化，终于完成。

思路：注意学会利用“模”这个看似无用的信息以简化运算，防止超时(TLE)和爆栈(RE)

不要尝试将递推暴力转化成通项，带根号2，计算机可能吃不消，PyCharm上面可以运行样例，提交时会报错。

真正写出来能AC的代码其实并不长。



代码

```python
pell = [0, 1]
for _ in range(1000000):
    pell.append((pell[-2] + 2 * pell[-1]) % 32767)


Lne = int(input())
for _ in range(Lne):
    print(pell[int(input())])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251103_003200](D:\腾讯电脑管家截图文件\局部截取_20251103_003200.png)

![局部截取_20251103_003213](D:\腾讯电脑管家截图文件\局部截取_20251103_003213.png)



### M46.全排列

backtracking, https://leetcode.cn/problems/permutations/

思路:

> 递归思路，不断由少一个元素的结果生成最终结果。

解题过程

> 先定义可调用的permute0，再敲定base(len(listy) == 1)，然后递归即可。

复杂度

- 时间复杂度: O(n*n!)
- 空间复杂度: O(n*n!)

代码

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute0(listy):
            if len(listy) == 1:
                return([[listy[0]]])
            else:
                al_listy = []
                for j_in_listy in listy:
                    n_listy = [j_in_listy]
                    listy0 = listy[:]
                    listy0.remove(j_in_listy)
                    for k_in_listyf in permute0(listy0):
                        for k_in_listy in k_in_listyf:
                            n_listy.append(k_in_listy)
                        al_listy.append(n_listy)
                        n_listy = [j_in_listy]
                return(al_listy)


        return(permute0(nums))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251103_003459](D:\腾讯电脑管家截图文件\局部截取_20251103_003459.png)

![局部截取_20251103_003517](D:\腾讯电脑管家截图文件\局部截取_20251103_003517.png)

![局部截取_20251103_003527](D:\腾讯电脑管家截图文件\局部截取_20251103_003527.png)

![局部截取_20251103_003733](D:\腾讯电脑管家截图文件\局部截取_20251103_003733.png)



### T02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/pctbook/T02754

耗时：做了整整一个下午。

思路：M46.全排列里面的函数可以搬过来用了。为简化运算，

最后应该逐个筛选正确选项(valid == True\blacklist == 0)

而不应该逐个排除错误选项(valid == False\blacklist != 0)。

blacklist==0表示合法这个是我个人的习惯，从两个月之前就这么写，当时还不能掌握bool型数据的用法，就用blacklist来替代。后来发现这种写法虽略耗时但却有可以表示更加复杂状态的优点，就一直这样用习惯了。



代码

```python
def k0j(listy):
    return ''.join(listy)


def _2sqr(x0, y0, x1, y1):
    if abs(x0 - x1) == abs(y0 - y1):
        return True
    else:
        return False


def permute0(listy):
    if len(listy) == 1:
        return [[listy[0]]]
    else:
        al_listy = []
        for j_in_listy in listy:
            n_listy = [j_in_listy]
            listy0 = listy[:]
            listy0.remove(j_in_listy)
            for k_in_listyf in permute0(listy0):
                for k_in_listy in k_in_listyf:
                    n_listy.append(k_in_listy)
                al_listy.append(n_listy)
                n_listy = [j_in_listy]
        return al_listy


al = permute0([1, 2, 3, 4, 5, 6, 7, 8])
bl = []
for a in al:
    blacklist = 0
    for i in range(0, 7):
        if blacklist == 0:
            for j in range(i + 1, 8):
                if _2sqr(i + 1, int(a[i]), j + 1, int(a[j])):
                    blacklist = 1
                    break

    if blacklist == 0:
        bl.append(a)


res = []
for a in bl:
    aa = []
    for b in a:
        aa.append(str(b))
    res.append(aa)
res.sort()

Lne = int(input())
for _ in range(Lne):
    n = int(input())
    print(k0j(res[n - 1]))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251103_005753](D:\腾讯电脑管家截图文件\局部截取_20251103_005753.png)

![局部截取_20251103_005809](D:\腾讯电脑管家截图文件\局部截取_20251103_005809.png)



### T01958 Strange Towers of Hanoi

http://cs101.openjudge.cn/practice/01958/

耗时：20min速通。

思路：其实有了M04147汉诺塔问题(Tower of Hanoi)的基础，再仔细读题，很轻松就能AC；

另一题29750:困难河内塔(只阅读了题目，也是和汉诺塔相关问题，并没有来得及做，截至11月3日00:00无一人通过)是真的难，以后有空再做。

代码

```python
def hanoi_3(n0):
    return 2 ** n0 - 1


def hanoi_4(n0):
    if n0 == 1:
        return 1
    elif n0 == 2:
        return 3
    else:
        listy_hanoi_4 = []
        for k0 in range(1, n0):
            jit_hanoi_4 = 2 * hanoi_4(n0 - k0) + hanoi_3(k0)
            listy_hanoi_4.append(jit_hanoi_4)
        return min(listy_hanoi_4)


for i in range(1, 13):
    print(hanoi_4(i))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![局部截取_20251103_005927](D:\腾讯电脑管家截图文件\局部截取_20251103_005927.png)

![局部截取_20251103_005936](D:\腾讯电脑管家截图文件\局部截取_20251103_005936.png)



## 2. 学习总结和收获



<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

LeetCode第474场周赛，这是我第一次参加Leetcode上的周赛，结果仅用45分钟就AC3，得到12分(11:00才想起比赛的事进去做题，11:45左右完成第三题)。

![局部截取_20251103_001134](D:\腾讯电脑管家截图文件\局部截取_20251103_001134.png)

![局部截取_20251103_000912](D:\腾讯电脑管家截图文件\局部截取_20251103_000912.png)

![局部截取_20251103_000932](D:\腾讯电脑管家截图文件\局部截取_20251103_000932.png)

![局部截取_20251103_001012](D:\腾讯电脑管家截图文件\局部截取_20251103_001012.png)
